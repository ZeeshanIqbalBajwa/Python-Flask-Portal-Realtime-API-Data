
from apps.home import blueprint
from flask import render_template, request,redirect,jsonify,url_for,session,flash
from flask_wtf import FlaskForm
from flask_login import login_required, logout_user
from jinja2 import TemplateNotFound

from apps.home.forms import ModelForm
from apps.home.utils import getToken, createSlice, getSLAPolicy,getSelectionPolicy,getMonitoringPolicy,getTransportSlice,deleteTransplantSlice,getNodeAndLink,updateLatecny,getNeNameForLink,getCore,getRan
import requests
import json

@blueprint.route('/')
# @login_required
def index():
    try:
        # api_url = "https://gorest.co.in/public/v1/users"
        # req = requests.get(api_url)
        data=getTransportSlice()
        return render_template('home/dashboard.html',newdata=data)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


@blueprint.route('/<template>',methods=['GET', 'POST'])
# @login_required
def route_template(template):

    try:
        if not template.endswith('.html'):
            template += '.html'


        segment = get_segment(request)
        # Detect the current page
        if 'csrf_token' in request.form:
            # read form data
            res=createSlice(request.form)
            # print(request.form)
            # print(request.form)
            if res == False:
                flash('Error While Creating Slice')
                return redirect(url_for('home_blueprint.index'))
            elif res == True:
                flash('Slice Created Successfully')
                return redirect(url_for('home_blueprint.index'))


        if(get_segment(request) == 'dashboard.html'):
            # print("session data", session)
            data = getTransportSlice()
            return render_template('home/dashboard.html', newdata=data)


        if template == 'model.html':
            model_form = ModelForm(request.form)
            print("model_form",model_form)
            # return render_template("home/" + template, segment=segment,form=model_form,tpsource=["RAN1","UPF1"],tpdestination=["RAN1","UPF1"],sla=getSLAPolicy(),monitor=getMonitoringPolicy(),selection=getSelectionPolicy())
            return render_template("home/" + template, segment=segment,form=model_form,tpsource=getRan(),tpdestination=getCore(),customerid=["PublicSafety","UCC","Citibank","RioTinto","LondonCity","Etisalat"],monitor=getMonitoringPolicy())
        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None

@blueprint.route('/_update_dropdown')
def update_dropdown():

    # the value of the first dropdown (selected by the user)
    selected_class = request.args.get('selected_class', type=str)

    # get values for the second dropdown
    # updated_values = get_dropdown_values()[selected_class]
    obj={
        "PublicSafety":["eMBB","URLLC","MIoT"],
        "UCC":["CCTV","IoT","eMBB"],
        "Citibank":["eMBB"],
        "RioTinto":["URLLC"],
        "LondonCity":["MIoT"],
        "Etisalat":["CCTV"]
    }
    for data in obj:
        if data == selected_class:
            updated_values = obj[selected_class]

    # create the value sin the dropdown as a html string
    html_string_selected = ''
    for entry in updated_values:
        html_string_selected += '<option value="{}">{}</option>'.format(entry, entry)

    return jsonify(html_string_selected=html_string_selected)

@blueprint.route('/delete/<string:id>')
def delete(id):
    try:
        print("delete",id)
        res = deleteTransplantSlice(id)
        if res == True:
            return 'success'
        else:
            return 'error'

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


@blueprint.route('/update/<string:linkid>/<int:latency>')
def update(linkid,latency):
    try:
        print("linkid",linkid,"latency", latency)
        res = updateLatecny(linkid,latency)
        if res == True:
            return 'success'
        else:
            return 'error'

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500

@blueprint.route('selection_policy')
def selection():
    try:
        list=getSelectionPolicy()
        return render_template('home/selection-policy.html', newdata=list)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


@blueprint.route('SLA_policy')
def SLA():
    try:
        list=getSLAPolicy()
        return render_template('home/SLA.html', newdata=list)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500

@blueprint.route('monitoring_policy')
def monitoring():
    try:
        list=getMonitoringPolicy()
        return render_template('home/monitoring-policy.html', newdata=list)


    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


@blueprint.route('link_listing')
def link():
    try:
        list=getNeNameForLink()
        return render_template('home/latency.html', newdata=list)


    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500