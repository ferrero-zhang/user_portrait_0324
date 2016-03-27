#-*- coding:utf-8 -*-
import os
import time
import json
from flask import Blueprint, url_for, render_template, request, abort, flash, session, redirect
from user_portrait.time_utils import ts2datetime
from User_sort_interface import user_sort_interface
from Offline_task import search_user_task


mod = Blueprint('user_rank', __name__, url_prefix='/user_rank')

@mod.route('/user_sort/', methods=['GET', 'POST'])
def user_sort():
    username = request.args.get('username', '')
    search_time = request.args.get('time', '')
    sort_norm = request.args.get('sort_norm', '')
    sort_scope = request.args.get('sort_scope', '')
    arg = request.args.get('arg', '')
    st = request.args.get('st', '')
    et = request.args.get('et', '')
    isall = request.args.get('all','')
    all = True
    if isall == 'True':
        all = True
    else :
        all = False
    if arg :
        pass
    else :
        arg = None
    results = user_sort_interface(username,search_time,sort_scope,sort_norm,arg,st,et,all)
    return json.dumps(results)

@mod.route('/search_task/', methods=['GET', 'POST'])
def search_task():
    username = request.args.get('username', '')
    results = search_user_task(username)
    return json.dumps(results)

