from flask import render_template, redirect, request
from voip import app
from voip.calls.models import cdr
from flask_login import login_required
from voip.calls.form import SearchCall
import boto3
import datetime
import config


client = boto3.client('s3', endpoint_url=str(config.Config.ENDPOINT_URL),
                      aws_access_key_id=str(config.Config.ACCESS_KEY),
                      aws_secret_access_key=str(config.Config.SECRET_KEY))


@app.route("/calls/search/", methods=["GET", "POST"])
@login_required
def calls_search():
    form = SearchCall()
    if form.is_submitted():
        data_from = form.data_from.data
        data_to = form.data_to.data
        number = form.numb.data

        if (data_from is None):
            return render_template("search_form.html", form=form)
        if(data_to is None):
            data_to = datetime.datetime.now()

        table = cdr.query.filter(((cdr.src.like("%"+number+"%")) | (cdr.dst.like("%"+number+"%"))) & ((cdr.calldate > data_from) & (cdr.calldate < data_to)))

        urlList = {}
        for key in table:
            urlList[key.uniqueid] = client.generate_presigned_url('get_object', Params={'Bucket': config.Config.S2_BUCKET, 'Key': 'main/'+key.uniqueid+'.mp3'})
        return render_template("search_result.html", table=table, urlList=urlList, i=0)
    return render_template("search_form.html", form=form)