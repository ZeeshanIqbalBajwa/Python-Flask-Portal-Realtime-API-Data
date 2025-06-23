from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import  DataRequired


class ModelForm(FlaskForm):
    slice_name = StringField('Slice Name',
                         id='slice_name',
                         validators=[DataRequired()])
    Service_type = StringField('Service type',
                         id='Service_type',
                         validators=[DataRequired()])
    Customer_Id = StringField('Customer Id',
                         id='Customer_Id',
                         validators=[DataRequired()])

    NS_ID = StringField('NS ID',
                         id='NS_ID',
                         validators=[DataRequired()])

    Service_IP_address = StringField('Service IP address',
                         id='Service_IP_address',
                         validators=[DataRequired()])
    SAP_IP_address = StringField('SAP IP address',
                         id='SAP_IP_address',
                         validators=[DataRequired()])
    TP_ID = SelectField('TP ID',
                         choices='TP_ID',
                         validators=[DataRequired()])
    VLAN = StringField('VLAN',
                         id='VLAN',
                         validators=[DataRequired()])
    serviceipaddress = StringField('Service IP address',
                         id='serviceipaddress',
                         validators=[DataRequired()])
    sapipaddress = StringField('SAP IP address',
                         id='sapipaddress',
                         validators=[DataRequired()])
    tpid = SelectField('TP ID',
                         choices='tpid',
                         validators=[DataRequired()])
    vlan1 = StringField('VLAN',
                         id='vlan1',
                         validators=[DataRequired()])
    selectionPolicy = SelectField('Selection Policy',
                         choices='selectionPolicy',
                         validators=[DataRequired()])
    monitoringPolicy = SelectField('Monitoring Policy',
                         choices='monitoringPolicy',
                         validators=[DataRequired()])
    SLAPolicy = SelectField('SLA Policy',
                         choices='SLAPolicy',
                         validators=[DataRequired()])
    connectionGroupName = StringField('Connection Group Name',
                            id='connectionGroupName',
                            validators=[DataRequired()])
