""" contains functionality for notebook iFDO_create.ipynb """

import os
import copy
import ipywidgets as widgets
import ast
import traitlets
import functools
import numpy as np
import markdown
import difflib
import requests
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from mpl_toolkits.mplot3d import Axes3D
from ipyfilechooser import FileChooser
from pprint import pprint

import mariqt.core as miqtc
import mariqt.variables as miqtv
import mariqt.tests as miqtt
import mariqt.geo as miqtg
import mariqt.sources.ifdo as miqtiFDO
import mariqt_widgets.notebook_widgets as miqtwidgets


UNKNOWNKEY = 'unknown'
MIN_HEADER_FIELDS = [
                     'image-set-uuid',
                     'image-set-ifdo-version',
                     'image-set-handle',
                     'image-context',
                     'image-project',
                     'image-event',
                     'image-platform',
                     'image-sensor',
                     'image-coordinate-reference-system',
                     'image-abstract',
                     'image-pi',
                     'image-creators',
                     'image-license',
                     'image-copyright',   
                     'image-set-local-path',
                     'image-set-name',
                     ]

# are not shown in the header sections
EXCLUDE_FROM_HEADER_FIELDS = [ "mpeg7",
                            #'image-acquisition-settings',
                            #'image-filename',
                            'image-uuid',
                            'image-hash-sha256',
                            'image-datetime',
                            'image-handle',
                            'longitude',
                            'latitude',
                            'image-depth',
                            'image-altitude',
                            'image-meters-above-ground'
                            'image-coordinate-uncertainty-meters',
                            'yaw','pitch','roll',
                            ]

FAKE_OUTPUT = widgets.Output()


def get_min_header_fields():
    ret = {}
    ifdo_fields = miqtc.get_ifdo_fields()

    for field in MIN_HEADER_FIELDS:
        ret[field] = ifdo_fields[field]
    return ret


def get_but_min_header_fields():
    ret = {}
    ifdo_fields = miqtc.get_ifdo_fields()

    for field in ifdo_fields:
        if field not in MIN_HEADER_FIELDS:
            ret[field] = ifdo_fields[field]
    return ret


class LoadedHeaderFields():
    """ proved a tracker for used loaded header fields to privide header fields that have not been used yet """
    def __init__(self,loadedFields:dict):
        if miqtv.image_set_header_key in loadedFields:
            self.loadedHeaderFields = loadedFields[miqtv.image_set_header_key]
        else:
            self.loadedHeaderFields = loadedFields
        self.unusedLoadedHeaderFields = copy.deepcopy(self.loadedHeaderFields)
        self.usedLoadedHeaderFields = {}

    def getHeaderField(self,field:str):
        if field in self.unusedLoadedHeaderFields:
            del self.unusedLoadedHeaderFields[field]
        if field in self.loadedHeaderFields:
            self.usedLoadedHeaderFields.update({field : self.loadedHeaderFields[field]})
            return self.loadedHeaderFields[field]
        else:
            return ""


class GridFieldWidgetCreator():
    """ Creates a grid view on fields and returns this widget """

    def __init__(self,fields:dict,loadedHeaderFields:LoadedHeaderFields,on_change_fct = None,optional = False):
        """ Creates a grid view on fields and returns this widget"""# and the a dict with field names as keys and their text and validation widget as a list value"""

        self.loadedHeaderFields = loadedHeaderFields
        self.on_change_fct = on_change_fct
        self.optional = optional

        fields = copy.deepcopy(fields)
        self.fieldValueWidgets = {}
        self.fields_widgets_dict = {}
        self.items = []

        try:
            on_change_fct(0)
        except Exception:
            def on_change_fct(change):
                pass
        
        for fieldName in fields:
            subFieldLevel = 0
            #print(fieldName)
            self.__createLine(self.items,fieldName,fields[fieldName],subFieldLevel,self.loadedHeaderFields,self.fields_widgets_dict)

        #self.gridWidget = widgets.GridBox(self.items, layout=widgets.Layout(width='100%',grid_template_columns='25% 5% 35% 34%'))
        self.gridWidget = widgets.GridBox(self.items, layout=widgets.Layout(width='100%',grid_template_columns='25% 40% 34%'))
        #gridWidget = widgets.GridBox(items, layout=widgets.Layout(width='100%',grid_template_columns='auto auto auto auto'))


    def getWidget(self):
        return self.gridWidget#, self.fieldValueWidgets

 
    def updateGridFieldValueWidgets(self, iFDO:miqtiFDO.iFDO):
        """ updates values in dict fieldValueWidgets with current values from iFDO tmp values"""
        for field in self.fieldValueWidgets:
            try:
                value = str(iFDO.findTmpField(field))
                if value != "":
                    self.fieldValueWidgets[field][0].value = value
            except miqtc.IfdoException:
                pass

    
    def _get_field_widget_value(self,fields_widgets:dict):
        ret = {}
        for key,val in fields_widgets.items():
            if isinstance(val,ValueWidgetObj):
                value = val.get_value()
            elif isinstance(val,dict):
                value = self._get_field_widget_value(val)
            elif isinstance(val,miqtwidgets.EditalbleListWidget):
                list_items = []
                for item in val.itemObjList:
                    list_items.append(item.itemWidget.getParams())
                value = list_items
            ret[key] = value
        return ret


    def getFieldsDict(self):
        """ returns dict to update iFDO header with fields and values from this widget. Throws iFDOException in case of invalid field """
        # TODO
        #print("self.fields_widgets_dict")
        #pprint(self.fields_widgets_dict)
        header_update = self._get_field_widget_value(self.fields_widgets_dict)
        # TODO
        #print("header_update")
        #pprint(header_update)
        
        return header_update

        # TODO
        header_update = {}
        levels = []
        for field in self.fieldValueWidgets:
            lowerstSubFieldName = field.split(":")[-1] # TODO the whole thing could be omitted if iFDO allowed for URN notation
            currentSubFieldLevel = self.fieldValueWidgets[field][2]
            levels = levels[0:currentSubFieldLevel]
            if isinstance(self.fieldValueWidgets[field][0],widgets.Label): # is subfield parent
                currentDict = self.__getCurrentDict(header_update,levels)
                currentDict[lowerstSubFieldName] = {}
                levels.append(lowerstSubFieldName)
                currentDict = self.__getCurrentDict(header_update,levels)
                continue
            else:
                currentDict = self.__getCurrentDict(header_update,levels)

            if self.fieldValueWidgets[field][1].disabled == True:
                    currentDict[lowerstSubFieldName] = ""
            else:
                if self.fieldValueWidgets[field][1].valid == True:
                    try:
                        val = ast.literal_eval(self.fieldValueWidgets[field][0].value.strip())
                    except Exception:
                        val = self.fieldValueWidgets[field][0].value
                    currentDict[lowerstSubFieldName] = val
                else:
                    raise miqtc.IfdoException("Invalid field: " + field)


        #TODO
        pprint(header_update)            
        
        return header_update


    # def __getCurrentDict(self,currentDict:dict,levels:list):
    #     if len(levels) == 0:
    #         return currentDict
    #     currentField = levels[0]
    #     levelsNew = levels[1::]
    #     currentDictNew = currentDict[currentField]
    #     return self.__getCurrentDict(currentDictNew,levelsNew)


    def __createLine(self, items:dict,fieldName,field:dict,subFieldLevel:int,loadedDataDict:dict,fields_widgets_dict:dict):

        #TODO
        #print(fieldName)

        # loaded value
        if isinstance(loadedDataDict,LoadedHeaderFields):   
            loadedValue = str(loadedDataDict.getHeaderField(fieldName))

            #TODO
            #print("loadedValue LoadedHeaderFields",loadedValue)

        else:
            try:
                loadedValue = str(loadedDataDict[fieldName.split(":")[-1]]) # subfields are not LoadedHeaderFields anymore
            except Exception:
                loadedValue = ""
            # TODO
            #print("loadedValue subfield",loadedValue)


        # label
        labelWidget = widgets.HBox([ miqtwidgets.MyLabel(fieldName.split(":")[-1]) ])
        # indentation
        labelWidget.layout =  widgets.Layout(padding='0px 0px 0px ' + str(20*subFieldLevel)+'px') 
        items.append(labelWidget)

        # info text
        comment = ""
        if 'description' in field:
            comment = field['description']
        info_text = miqtwidgets.MyScrollbox(value=comment)

        dataType = str
        jsonschema = None
        if 'type' in field:
            dataType = miqtc.jsonschmea_type_2_python_type(field['type'])
            jsonschema = field

        if dataType == dict:
            # e.g. image-acquisition-settings, is of type obj but not defined
            if 'properties' in field:
                #dataType = str
            #else:
                items += [widgets.Label()]*1 + [info_text] # placeholder
                self.fieldValueWidgets[fieldName] = widgets.Label(), widgets.Label(), subFieldLevel # placeholder
                fields_widgets_dict[fieldName] = {}
                for subField in field['properties']:
                    try:
                        loadedValue_ = ast.literal_eval(loadedValue)
                    except Exception:
                        loadedValue_ = ""
                    #fields_widgets_dict[fieldName][subField] = {}
                    #self.__createLine(items,fieldName+":"+subField,field['properties'][subField],subFieldLevel+1,loadedValue_,fields_widgets_dict[fieldName])
                    self.__createLine(items,subField,field['properties'][subField],subFieldLevel+1,loadedValue_,fields_widgets_dict[fieldName])
                    
                return

        # TODO
        # create extra widget for array of object items. Arrays as scalars etc. can still be displayed as strings to save space
        if dataType == list and 'properties' in field['items']:

            showValidWidget = widgets.Label() # validWidget placeholder
            #items.append(showValidWidget)

            loadedValuesList = loadedValue
            if isinstance(loadedValuesList,str) and not loadedValuesList == "":
                    loadedValuesList = ast.literal_eval(loadedValuesList)
            if not isinstance(loadedValuesList,list):
                loadedValuesList = [loadedValuesList]
            loadedValuesList = [i for i in loadedValuesList if i != '']
            
            # TODO
            #print("loadedValuesList",loadedValuesList)

            item_fields = field['items']['properties']

            arrayItemValueWidget = ArrayObjectItemValueWidget(on_change_fct=self.on_change_fct,
                                                        field_name=fieldName,
                                                        item_fields=item_fields,
                                                        source_list=loadedValuesList,
                                                        optional = self.optional)

            valueWidget = miqtwidgets.EditalbleListWidget(label='',itemWidgetExample=arrayItemValueWidget,iFDOList=loadedValuesList,repaint_after_delete=False)
            valueWidget.observe(self.on_change_fct,names='value')
            valid_plus_value_widget = valueWidget.completeWidget

            fields_widgets_dict[fieldName] = valueWidget

        # simple single item    
        else:
            
            # valid
            showValidWidget =  miqtwidgets.MyValid(
                valid=False
                )
            #items.append(showValidWidget)
            valueWidget = self._get_value_widget(fieldName, field, loadedValue)
            valueWidget.observe(self.on_change_fct,names='value')

            fields_widgets_dict[fieldName] = ValueWidgetObj(fieldName,valueWidget,showValidWidget,dataType)

            if fieldName == 'image-set-uuid' or fieldName == 'image-set-ifdo-version':
                valueWidget.disabled = True

            if fieldName == 'image-platform' or fieldName == 'image-sensor':
                dataType = 'equipmentID'

            msg_widget = widgets.HBox([])
            validator = Validator(showValidWidget, dataType, valueWidget.value,optional = self.optional,jsonschema=jsonschema,msg_widget=msg_widget)
            valueWidget.observe(validator.handle_observe, names='value')

            valid_plus_value_widget = widgets.GridBox([showValidWidget, valueWidget,widgets.HBox([]),msg_widget], layout=widgets.Layout(width='100%',grid_template_columns='10% 89%',))
        
            

        #items.append(valueWidget)
        items.append(valid_plus_value_widget)
        self.fieldValueWidgets[fieldName] = valueWidget, showValidWidget, subFieldLevel

        items.append(info_text)


    @staticmethod
    def _get_value_widget(field_name:str,field:dict, loadedValue:str):
        """ Return widget depending on fields type """


        # editable value
        # if 'type' in field and field['type'] == miqtv.dataTypes.text:
        #     valueWidget = widgets.Textarea(
        #             value=loadedValue,
        #             description='',
        #             disabled=False,
        #             layout=widgets.Layout(width='95%', height='60px'),
        #         )
        #     if fieldName == 'image-abstract':
        #         dataType = 'abstract'
        #         valueWidget.layout.height = '150px'
                #valueWidget.placeholder=miqtv.ifdo_coreFields['image-abstract']['comment'],

        if 'enum' in field:
            options_ = field['enum']
            if options_[-1] != UNKNOWNKEY:
                options_.append(UNKNOWNKEY)
            
            customValuesAllowed =False
            # TODO does that case even exist?
            # if miqtv.keyValidPlusCustom in options_:
            #     customValuesAllowed = True
            #     options_.remove(miqtv.keyValidPlusCustom)

            if loadedValue == "":
                loadedValue = options_[-1]
            elif loadedValue not in options_ and not customValuesAllowed:
                #print("Error: Invalid value \"" + loadedValue + "\" found for field \"" + fieldName + "\". Value not loaded.")   
                pass             
            
            if customValuesAllowed:
                valueWidget = widgets.Combobox(
                    options = options_,
                    value=loadedValue,
                    description='',
                    disabled=False,
                    layout=widgets.Layout(width='95%'),)
            else:
                valueWidget = widgets.Dropdown(
                    options = options_,
                    description='',
                    disabled=False,
                    layout=widgets.Layout(width='95%'),)
                if loadedValue in options_:
                    valueWidget.value = loadedValue
        else:
            # text widget
            if bool([e for e in ['abstract','description','objective','target','constraints','protocol'] if(e in field_name)]):
                valueWidget = widgets.Textarea(
                        value=loadedValue,
                        description='',
                        disabled=False,
                        layout=widgets.Layout(width='95%', height='60px'),
                    )
                if field_name == 'image-abstract':
                    dataType = 'abstract'
                    valueWidget.layout.height = '150px'
            else:
                valueWidget = widgets.Text(
                    value=loadedValue,
                    placeholder='unknown',
                    description="",
                    disabled=False,
                    layout=widgets.Layout(width='95%'),
                )
        return valueWidget
    

class ValueWidgetObj():
    """ Field object get current value from """

    def __init__(self,field_name,value_widget, valid_widget:miqtwidgets.MyValid,data_type:type,on_change_fct=None):
        self.value_widget = value_widget # must have .valid
        self.valid_widget = valid_widget
        self.field_name = field_name
        self.data_type = data_type

    def get_value(self):
        
        if self.valid_widget.disabled:
            return ""
        if not self.valid_widget.valid:
            raise miqtc.IfdoException('Invalid field: ' + self.field_name)
        if self.value_widget.value == '':
            return ''
        
        if self.data_type == str:
            return str(self.value_widget.value)
        if self.data_type == float:
            return float(self.value_widget.value)
        if self.data_type == int:
            return int(self.value_widget.value)
        if self.data_type == list or self.data_type == dict:
            return ast.literal_eval(self.value_widget.value)
        print("Unhandled data type:" + str(self.data_type))
        return str(self.value_widget.value)
    
    def set_value(self,value):
        self.value_widget.value = value
        # TODO evaluate?


class ArrayObjectItemValueWidget(miqtwidgets.ItemWidgetBase):

    def __init__(self,on_change_fct,field_name:str,item_fields:dict,source_list:list,optional = False):
        """
        fixedItemWidthPixels: if None item width is adjusted to space, otherways width is fix and scroll area is created if needed
        """
        miqtwidgets.ItemWidgetBase.__init__(self,on_change_fct)
        self.on_change_fct = on_change_fct # TODO needed if observe works?
        self.field_name = field_name
        self.item_fields = item_fields
        self.optional = optional
        self.source_list = source_list

        self.widgets_dict = {}
        self.msg_widgets_dict = {}
        for key, val in self.item_fields.items():
            valid_plus_value_widget = self.create_ValueWidgetObj(key,val)
            msg_widget = widgets.HBox([])
            self._add_validator(field=val,valid_plus_value_widget=valid_plus_value_widget,msg_widget=msg_widget)
            self.widgets_dict[key] = valid_plus_value_widget
            self.msg_widgets_dict[key] = msg_widget
        self._repaint()


    def _repaint(self):
        items = []
        for key,val in self.widgets_dict.items():
            items += [widgets.Label(val.field_name),val.valid_widget, val.value_widget,
                      widgets.HBox([]),widgets.HBox([]),self.msg_widgets_dict[key]]
        self.widget = widgets.GridBox(items, layout=widgets.Layout(width='100%',grid_template_columns='20% 10% 67.5%'))

    
    def _add_validator(self,field:dict,valid_plus_value_widget:ValueWidgetObj,msg_widget):
        dataType = str
        jsonschema = None
        if 'type' in field:
            dataType = miqtc.jsonschmea_type_2_python_type(field['type'])
            jsonschema = field
        validator = Validator(valid_plus_value_widget.valid_widget, dataType, 
                              valid_plus_value_widget.value_widget.value,optional = self.optional,jsonschema=jsonschema,
                              msg_widget=msg_widget)
        valid_plus_value_widget.value_widget.observe(validator.handle_observe, names='value')


    def create_ValueWidgetObj(self,name:str,field:dict):
        valid_widget = miqtwidgets.MyValid( valid=False)
        value_widget = GridFieldWidgetCreator._get_value_widget(name, field,"")
        if 'type' in field:
            data_type = miqtc.jsonschmea_type_2_python_type(field['type'])
        else:
            data_type = str
            #print("type not defined in",self.field_name,name,"!")
        return ValueWidgetObj(name,value_widget,valid_widget,data_type)


    def observe(self, handler, names=traitlets.All, type="change"):
        for key,val in self.widgets_dict.items():
            val.value_widget.observe(handler,names,type)


    def copy(self):
        ret = ArrayObjectItemValueWidget(self.on_change_fct,self.field_name,self.item_fields,self.optional)
        return ret
    

    def setParams(self,params:dict):
        if params == []:
            return
        if not isinstance(params,dict):
            print("Error, this shoud be a dict! I'm in mariqt-widgets ifdo_create.py setParams", params)
            raise miqtc.IfdoException('Error, this shoud be a dict!: ' + str(params))
        else:
            # reset
            for key,val in self.widgets_dict.items():
                if key in params:
                    value = params[key]
                else:
                    value = ""
                val.set_value(value)
            # TODO there could be the case where there was a additional property which should be removed
            for key,val in params.items():
                if key not in self.widgets_dict:
                    self.widgets_dict[key] = self.create_ValueWidgetObj(key,{})
                    msg_widget = widgets.HBox([])
                    self._add_validator(field={},valid_plus_value_widget=self.widgets_dict[key],msg_widget=msg_widget)
                    self.widgets_dict[key].set_value(val)
                    self.msg_widgets_dict[key] = msg_widget
                    self._repaint()
        
        
    def getParams(self):
        ret = {}
        for key,val in self.widgets_dict.items():
            ret[key] = val.get_value()
        return ret
        

    def getWidget(self):
        return self.widget
        

    def removeFromSource(self,params):
        """ what should be done in source if item with params deleted? """
        pass # not needed since repaint_after_delete == False
        # print("params",params)
        # print("self.source_list",self.source_list)
        # if params in self.source_list:
        #     self.source_list.remove(params)
        #     print("removed")
        

    def readParamsFromElement(self,element):
        """ how can params be read from the one source element in order to init widget """
        ret = element
        if isinstance(element,str):
            ret = ast.literal_eval(element)
        if not isinstance(ret,dict):
            miqtc.IfdoException("Error, this shoud be a dict! I'm in mariqt-widgets ifdo_create.py readParamsFromElement")
        return ret


class Validator():

    def __init__(self,showValidWidget, dataType:type, initValue, optional:bool=False, jsonschema = None, msg_widget:widgets.HBox=None,empty_is_valid=True):
        self.dataType = dataType
        self.jsonschema = jsonschema
        self.showValidWidget = showValidWidget
        self.optional = optional
        self.msg_widget = msg_widget
        self.empty_is_valid = empty_is_valid
        change = {}
        change['new'] = initValue
        self.handle_observe(change)


    def handle_observe(self,change):
        value = change['new']
        valid = False
        warning = False

        if (value == UNKNOWNKEY or value == "") and self.optional:
            self.showValidWidget.disabled = True
        else:
            self.showValidWidget.disabled = False

        if value == "":
            warning = True
            if not self.empty_is_valid:
                valid = False
                warning = False

        if self.dataType == 'abstract':
            warning = True
            if len(value) > 500 and len(value) < 2000:
                valid = True
                warning = False
        elif self.dataType == float:
            try:
                value = float(value)
                valid = True
            except Exception:
                pass
        elif self.dataType == int:
            try:
                value = int(value)
                valid = True
            except Exception:
                pass
        elif self.dataType == dict or self.dataType == list:
            try:
                value = ast.literal_eval(value)
                valid = True
            except Exception:
                pass
        # TODO
        elif self.dataType == 'email':
            warning = True
            valid = miqtt.isValidEmail(value)
            if valid: warning = False
        # TODO
        elif self.dataType == "orcid":
            warning = True
            valid = miqtt.isValidOrcid(value)
            if valid: warning = False
        elif self.dataType == dict:
            try:
                val = eval(value)
                if isinstance(val,dict):
                    valid = True
            except Exception:
                pass 
        # TODO
        elif self.dataType == 'equipmentID':
            warning = True
            with FAKE_OUTPUT:
                valid = miqtt.isValidEquipmentID(value)
            if valid: warning = False    
        else:
            warning = True
            if value != "" and value != UNKNOWNKEY:
                valid = True
                warning = False

        if not self.jsonschema is None:
            valid, msg = miqtt.validate_against_schema(value,self.jsonschema)

            # check if uri online
            if valid and 'format' in self.jsonschema and self.jsonschema['format'] == 'uri':
                try:
                    ret = requests.head(value)
                    if ret.status_code != 200:
                        raise Exception()
                except Exception:
                    warning = True
                    msg = "Caution, not online."

            if self.msg_widget is not None:
                if (not valid  or warning) and msg != "" and value != "":
                    color = 'red'
                    if warning:
                        color = 'orange'
                    label = widgets.HTML(value = f"<b><font color={color}>{msg}</b>")
                    #label = widgets.Label(msg)
                    self.msg_widget.children = [label]
                else:
                    self.msg_widget.children = []


        self.showValidWidget.valid = valid
        self.showValidWidget.warning = warning



######## Tabs ###################################################################################################

class TabsCommon():
    """ contains common variables of all tabs """
    def __init__(self,on_nextTabButtonClick, on_tabDevalidated, counter:list, tabsList:list):
        self.on_nextTabButtonClick = on_nextTabButtonClick
        self.on_tabDevalidated = on_tabDevalidated
        self.counter = counter
        self.tabsList = tabsList
        

class TabBase():
    """ Tab base class containing 'Next' button and its functionality """
    
    def __init__(self,tabsCommon:TabsCommon):
        
        self.tabsCommon = tabsCommon
        self.index = len(self.tabsCommon.tabsList)
        self.tabsCommon.tabsList.append(self)
        self.nextTabButton = widgets.Button(description = "Next", disabled = True)
        self.setButton = widgets.Button(description="Set")
        self.setButton.style.button_color = '#87CEFA'
        self.nextTabButton.on_click(functools.partial(self.tabsCommon.on_nextTabButtonClick,counter = self.tabsCommon.counter))
        self.outputWidget = widgets.HTML()
        
    
    def tabValidate(self,valid):
        if valid:
            self.nextTabButton.disabled = False
            self.nextTabButton.style.button_color = 'lightgreen'
            self.setButton.style.button_color = '#F5F5F5'
        else:
            if not self.nextTabButton.disabled:
                self.nextTabButton.disabled = True
                self.nextTabButton.style.button_color = '#F5F5F5'
                self.setButton.style.button_color = '#87CEFA'
                self.tabsCommon.on_tabDevalidated(self.index)
            
    def tabValidated(self):
        return self.nextTabButton.disabled
    
    def writeToOutputWidget(self,msg:str):
        self.outputWidget.value = miqtwidgets.escapeHTML(msg) 
        
    def onTabSelected(self,index):
        """ is called when ever a new tab is selected. Calls _onTabSelected if it's this tab that is selected """
        if int(index['new']) == self.index:
            self._onTabSelected()

    def _onTabSelected(self): # pseudo private as private functions can not be overwritten by child
        """ is called when tab is selected. Can be overwritten by child """
        pass
            
    def getWidget(self):
        raise NotImplementedError("Please Implement this method")
        
    def getTitle(self):
        raise NotImplementedError("Please Implement this method")
        
    def on_change_fct(self):
        raise NotImplementedError("Please Implement this method")




##### TAB: Start ################################


class Tab_initCoreFields(TabBase):
    """ This tab is manly required to prevent jupyter notebook from putting the tab widget in a scroll area by making the first tab rather small """
    
    def __init__(self,tabsCommon:TabsCommon):
        TabBase.__init__(self,tabsCommon)
        
        # markdownd text, CAUTION may not be indented
        textWidget = miqtwidgets.MarkdownWidget("""

**Great!** You provided your data in a valid directory structure. Now the iFDO creation can begin.

This **iFDO Creation Wizard** will walk you through all necessary steps one by one. Once you successfully finished one step the **Next** button at the end of the site will be activated and you can continue to the next step. Let's go!

            """)
        
        self.myWidget = widgets.VBox([miqtwidgets.VerticalSpacer(30),textWidget,miqtwidgets.VerticalSpacer(30),self.nextTabButton])
        
        self.tabValidate(True)
        
    def getWidget(self):
        return self.myWidget
    
    def getTitle(self):
        return "Start"
    
    def on_change_fct(self):
        pass


##### TAB: Core Header Fields ################################
    

class Tab_CoreHeaderFields(TabBase):
    
    def __init__(self,tabsCommon:TabsCommon,iFDO,loadedHeaderFields):
        TabBase.__init__(self,tabsCommon)
        
        # markdownd text, CAUTION may not be indented
        textWidget = miqtwidgets.MarkdownWidget("""
## Providing Core Information 

In order to create an iFDO file achieving FAIRness at least all the **core fields** should be provided.

### Core Header Fields

Please fill in the following for you project:
            """)

        # set button
        self.outputSetButton = widgets.Output()
        #setButton = widgets.Button(description="Set")
        #setButton.style.button_color = 'AliceBlue'
        self.notSetYetWarning = "" #"Values NOT set yet! Press 'Set' before you continue."
        self.setInfoLabel = widgets.Label(value = self.notSetYetWarning)
        setWidget = widgets.HBox([self.setButton,self.setInfoLabel])
        
        def on_setButton_clicked(b):
            self.outputSetButton.clear_output()
            with self.outputSetButton:
                
                # for e in ([PI_widget] + creatorsWidgets):
                #     if e.invalidField()[0]:
                #         self.writeToOutputWidget("Invalid field: " + e.invalidField()[1])
                #         return
                # min_header_info = {
                #     'image-creators':   [e.asDict() for e in creatorsWidgets],
                #     'image-pi':         PI_widget.asDict()
                # }
                try:
                    header_update = {**self.gridFieldWidgetCreator_remaining_min_header.getFieldsDict(),
                                     **self.imageSetNameWidgetCreator.getFieldsDict()}
                except miqtc.IfdoException as e:
                    self.writeToOutputWidget(str(e.args[0]))
                    return
                #min_header_info.update(header_update)

                """ for field,value in min_header_info.items():
                    if value == "":
                        self.writeToOutputWidget("Invalid field: " + field)
                        return """

                msg = ""
                try:
                    #iFDO.updateiFDOHeaderFields(min_header_info)
                    iFDO.update_ifdo_header_fields(header_update)
                except Exception as ex:
                    msg += ex.args
                    
                if msg == "":
                    self.setInfoLabel.value = ""
                    msg = "Values set."
                    self.tabValidate(True)
                
                self.writeToOutputWidget(msg)

        self.setButton.on_click(on_setButton_clicked)
        
        remaining_min_header_fields = get_min_header_fields()
        #remaining_min_header_fields_withAlts = {}
        remaining_min_header_fields_withoutAlts = {}
        imageSetNameField = {}
        for field in remaining_min_header_fields:
            #if 'alt-fields' in remaining_min_header_fields[field] and remaining_min_header_fields[field]['alt-fields'] != [] and remaining_min_header_fields[field]['alt-fields'] != ['']:
            #if field not in OMITTABLE_HEADER_FIELDS_IN_ALL_ITEMS and field not in EXCLUDE_FROM_HEADER_FIELDS:
            if field not in EXCLUDE_FROM_HEADER_FIELDS:
                if field == "image-set-name":
                    imageSetNameField.update({field : remaining_min_header_fields[field]})
                else:
                    remaining_min_header_fields_withoutAlts.update({field : remaining_min_header_fields[field]})

        self.gridFieldWidgetCreator_remaining_min_header = GridFieldWidgetCreator(remaining_min_header_fields_withoutAlts, loadedHeaderFields, self.on_change_fct)

        gridWidget_minHeaderWithoutAlts = self.gridFieldWidgetCreator_remaining_min_header.getWidget()

        # image-set-name widget
        self.imageSetNameWidgetCreator = GridFieldWidgetCreator(imageSetNameField, loadedHeaderFields, self.on_change_fct)
        setImageSetNameButton = widgets.Button(description="Construct", layout=widgets.Layout(width='80px'))
        def on_setImageSetNameButton_clicked(b):
            currentFields = self.gridFieldWidgetCreator_remaining_min_header.getFieldsDict()
            image_set_name = miqtiFDO.iFDO.constructImageSetName(currentFields['image-project']['name'],
                                                                                                currentFields['image-event']['name'],
                                                                                                currentFields['image-sensor']['name'])
            found = False
            for key,val in self.imageSetNameWidgetCreator.fields_widgets_dict.items():
                if isinstance(val,ValueWidgetObj) and val.field_name == 'image-set-name':
                    val.set_value(image_set_name)
                    found = True
                    self.on_change_fct(0)
                    break
            if not found:
                print("Field image-set-name not found and not updated!")
            
        setImageSetNameButton.on_click(on_setImageSetNameButton_clicked)
        items = self.imageSetNameWidgetCreator.items[0:1] + [setImageSetNameButton] + self.imageSetNameWidgetCreator.items[1::]
        #imageSetNameWidget = widgets.GridBox(items, layout=widgets.Layout(width='100%',grid_template_columns='15% 10% 5% 35% 34%'))
        imageSetNameWidget = widgets.GridBox(items, layout=widgets.Layout(width='100%',grid_template_columns='15% 10% 40% 34%'))


        # button set image-event uri to OSIS event url
        self.set_event_uri_button = widgets.Button(description="Try set OSIS event URL", layout=widgets.Layout(width='170px'))
        self.set_event_uri_button_msg_box = widgets.Output() #miqtwidgets.MyScrollbox()
        self.set_event_uri_button.on_click(self.on_set_event_uri_button_clicked)
        set_event_uri_button_line = [widgets.Label(),widgets.HBox([self.set_event_uri_button,self.set_event_uri_button_msg_box]),widgets.Label()]
        # squeeze button in
        updated_list_gridWidget_minHeaderWithoutAlts_chidren = list(gridWidget_minHeaderWithoutAlts.children)
        self._insert_line_bellow(updated_list_gridWidget_minHeaderWithoutAlts_chidren,'image-event',set_event_uri_button_line)
        gridWidget_minHeaderWithoutAlts.children = updated_list_gridWidget_minHeaderWithoutAlts_chidren

        # button set image-project uri to OSIS expedition url
        self.set_project_uri_button = widgets.Button(description="Try set OSIS exp. URL", layout=widgets.Layout(width='170px'))
        self.set_project_uri_button_msg_box = widgets.Output() #miqtwidgets.MyScrollbox()
        self.set_project_uri_button.on_click(self.on_set_project_uri_button_clicked)
        set_project_uri_button_line = [widgets.Label(),widgets.HBox([self.set_project_uri_button,self.set_project_uri_button_msg_box]),widgets.Label()]
        # squeeze button in
        updated_list_gridWidget_minHeaderWithoutAlts_chidren = list(gridWidget_minHeaderWithoutAlts.children)
        self._insert_line_bellow(updated_list_gridWidget_minHeaderWithoutAlts_chidren,'image-project',set_project_uri_button_line)
        gridWidget_minHeaderWithoutAlts.children = updated_list_gridWidget_minHeaderWithoutAlts_chidren

        # button set image-semspr uri to equipment url
        self.set_sensor_uri_button = widgets.Button(description="Try set equipment URL", layout=widgets.Layout(width='170px'))
        self.set_sensor_uri_button_msg_box = widgets.Output() #miqtwidgets.MyScrollbox()
        self.set_sensor_uri_button.on_click(self.on_set_sensor_uri_button_clicked)
        set_sensor_uri_button_line = [widgets.Label(),widgets.HBox([self.set_sensor_uri_button,self.set_sensor_uri_button_msg_box]),widgets.Label()]
        # squeeze button in
        updated_list_gridWidget_minHeaderWithoutAlts_chidren = list(gridWidget_minHeaderWithoutAlts.children)
        self._insert_line_bellow(updated_list_gridWidget_minHeaderWithoutAlts_chidren,'image-sensor',set_sensor_uri_button_line)
        gridWidget_minHeaderWithoutAlts.children = updated_list_gridWidget_minHeaderWithoutAlts_chidren

        # button set image-semspr uri to equipment url
        self.set_pfm_uri_button = widgets.Button(description="Try set equipment URL", layout=widgets.Layout(width='170px'))
        self.set_pfm_uri_button_msg_box = widgets.Output() #miqtwidgets.MyScrollbox()
        self.set_pfm_uri_button.on_click(self.on_set_pfm_uri_button_clicked)
        set_pfm_uri_button_line = [widgets.Label(),widgets.HBox([self.set_pfm_uri_button,self.set_pfm_uri_button_msg_box]),widgets.Label()]
        # squeeze button in
        updated_list_gridWidget_minHeaderWithoutAlts_chidren = list(gridWidget_minHeaderWithoutAlts.children)
        self._insert_line_bellow(updated_list_gridWidget_minHeaderWithoutAlts_chidren,'image-platform',set_pfm_uri_button_line)
        gridWidget_minHeaderWithoutAlts.children = updated_list_gridWidget_minHeaderWithoutAlts_chidren

        

        self.myWidget = widgets.VBox([   
                                textWidget,
                                miqtwidgets.VerticalSpacer(30),
                                #personsWidget,
                                gridWidget_minHeaderWithoutAlts,
                                imageSetNameWidget,
                                miqtwidgets.VerticalSpacer(30),
                                miqtwidgets.VerticalSpacer(30),
                                setWidget,
                                self.outputWidget,
                                self.outputSetButton,
                                miqtwidgets.VerticalSpacer(30),
                                self.nextTabButton,
                            ])
        

    def on_set_event_uri_button_clicked(self,b):
        event_uri_value_widget = self.gridFieldWidgetCreator_remaining_min_header.fields_widgets_dict['image-event']['uri'] 
        tmp_ifdo = {'image-set-header': {   **self.gridFieldWidgetCreator_remaining_min_header.getFieldsDict(),
                                            **self.imageSetNameWidgetCreator.getFieldsDict()},
                    'image-set-items': {} }
        self.set_event_uri_button_msg_box.clear_output()
        with self.set_event_uri_button_msg_box:
            try:
                uri = miqtiFDO.iFDO.get_header_image_event_uri_to_osis_event_url(tmp_ifdo)
                event_uri_value_widget.set_value(uri)
            except Exception as e:
                print("Failed ot get info from osis: " + str(e))

    def on_set_project_uri_button_clicked(self,b):
        project_uri_value_widget = self.gridFieldWidgetCreator_remaining_min_header.fields_widgets_dict['image-project']['uri'] 
        tmp_ifdo = {'image-set-header': {   **self.gridFieldWidgetCreator_remaining_min_header.getFieldsDict(),
                                            **self.imageSetNameWidgetCreator.getFieldsDict()},
                    'image-set-items': {} }
        self.set_project_uri_button_msg_box.clear_output()
        with self.set_project_uri_button_msg_box:
            try:
                uri = miqtiFDO.iFDO.get_header_image_project_uri_to_osis_expedition_url(tmp_ifdo)
                project_uri_value_widget.set_value(uri)
            except Exception as e:
                print("Failed ot get info from osis: " + str(e))

    def on_set_sensor_uri_button_clicked(self,b):
        sensor_uri_value_widget = self.gridFieldWidgetCreator_remaining_min_header.fields_widgets_dict['image-sensor']['uri'] 
        tmp_ifdo = {'image-set-header': {   **self.gridFieldWidgetCreator_remaining_min_header.getFieldsDict(),
                                            **self.imageSetNameWidgetCreator.getFieldsDict()},
                    'image-set-items': {} }
        self.set_sensor_uri_button_msg_box.clear_output()
        with self.set_sensor_uri_button_msg_box:
            uri = miqtiFDO.iFDO.get_header_equipment_uri_to_equipment_git_url(tmp_ifdo,'image-sensor')
        sensor_uri_value_widget.set_value(uri)

    def on_set_pfm_uri_button_clicked(self,b):
        pfm_uri_value_widget = self.gridFieldWidgetCreator_remaining_min_header.fields_widgets_dict['image-platform']['uri'] 
        tmp_ifdo = {'image-set-header': {   **self.gridFieldWidgetCreator_remaining_min_header.getFieldsDict(),
                                            **self.imageSetNameWidgetCreator.getFieldsDict()},
                    'image-set-items': {} }
        self.set_pfm_uri_button_msg_box.clear_output()
        with self.set_pfm_uri_button_msg_box:
            uri = miqtiFDO.iFDO.get_header_equipment_uri_to_equipment_git_url(tmp_ifdo,'image-platform')
        pfm_uri_value_widget.set_value(uri)


    def _insert_line_bellow(self,grid_items,field_name,line_items:list):
        i = 0
        stop = False
        for widget in grid_items:
            if isinstance(widget,widgets.HBox):
                for sub_widget in list(widget.children):
                    if isinstance(sub_widget,miqtwidgets.MyLabel):
                        if sub_widget.myvalue == field_name:
                            stop = True
                            break
            if stop:
                break
            i += 1
        offset = 9
        insert_pos = i + offset
        grid_items[insert_pos:insert_pos] = line_items

    
    def on_change_fct(self,change=None):
        #with miqtwidgets.Capturing() as output:
        
        self.setInfoLabel.value =  self.notSetYetWarning
        self.outputSetButton.clear_output()
        self.outputWidget.value = ""
        self.tabValidate(False)
        #debugOutputWidget.addText(str(output))
    
    def getWidget(self):
        return self.myWidget
    
    def getTitle(self):
        return "Core Fields"
    


##### TAB: Core Item Fields - UUID ################################
    

class Tab_CoreItemUUID(TabBase):
    
    def __init__(self,tabsCommon:TabsCommon,iFDO):
        TabBase.__init__(self,tabsCommon)
        
        # markdownd text, CAUTION may not be indented
        textWidget = miqtwidgets.MarkdownWidget("""
## Providing Core Information 

In order to create an iFDO file achieving FAIRness at least all the **core fields** should be provided.

### UUIDs

It is required that each image item gets a unique ID (UUID version 4). This ID must be stored in the image file itself. 

* For **photos** """ + str(miqtv.photo_types) + """ it is to be stored in the file's exif header field *ImageUniqueID* applying the [ExifTool](https://exiftool.org/).

* For **videos** """ + str(miqtv.video_types) + """ it is to be stored in the file's *Xmp.dc.identifier* field e.g. appyling the [Python XMP Toolkit](https://python-xmp-toolkit.readthedocs.io/en/stable/index.html) or in case of mkv to the *SegmentUID* using [mkvtoolnix](https://mkvtoolnix.download/downloads.html).

You can use the [AddUUIDsToFiles](https://gitlab.hzdr.de/datahub/marehub/ag-videosimages/mariqt-notebooks) notebook to add missing UUIDs.
            """)
        
        
        checkUUIDButton = widgets.Button(description = "Check UUIDs")

        self.uuidButtonOutput = widgets.Output()

        def on_checkUUIDButton_click(b):
            self.uuidButtonOutput.clear_output()
            with self.uuidButtonOutput:
                success, msg = iFDO.create_uuid_file()
                if not success:
                    print("Not all images contain valid UUIDs")
                else:
                    print("All images contain valid UUIDs")
                self.tabValidate(success)
                    
        checkUUIDButton.on_click(on_checkUUIDButton_click)        
        
        self.myWidget = widgets.VBox([textWidget,
                                      checkUUIDButton,
                                      self.uuidButtonOutput,
                                      miqtwidgets.VerticalSpacer(30),
                                      self.nextTabButton])
        
                
    def on_checkButton_clicked(self,b):
        self.tabValidate(True)
        
    def getWidget(self):
        return self.myWidget
    
    def getTitle(self):
        return "UUIDs"
    
    def on_change_fct(self):
        self.uuidButtonOutput.clear_output()
        self.tabValidate(False)




##### TAB: Core Item Fields - Navigation ################################

class NavigationFieldWidget():

    def __init__(self,fieldName:str,iFDOImageSetFieldName:str,loadedHeaderFields,on_change_fct,columnOptions:list=[],optional:bool=False,invertOption:bool=False,empty_is_valid=True):
        
        self.iFDOImageSetFieldName = iFDOImageSetFieldName
        self.fieldLabel = miqtwidgets.MyLabel(value = fieldName)
        self.checkNavFile = widgets.Checkbox(value=False,indent=False)
        self.columnName = widgets.Dropdown(
            options=columnOptions,
            layout=widgets.Layout(width='100%')
        )
        if invertOption:
            self.checkInvert = widgets.Checkbox(value=False,indent=False)
        else:
            self.checkInvert = widgets.HBox([])# placeholder
        self.checkSetValue = widgets.Checkbox(value=False,indent=False)
        self.setValueCheck = miqtwidgets.MyValid(valid=False)
        self.setValue = widgets.Text(value=str(loadedHeaderFields.getHeaderField(iFDOImageSetFieldName)),placeholder = "Set Value",layout=widgets.Layout(width='auto'))
        
        if iFDOImageSetFieldName in miqtc.get_ifdo_fields():
            descr = miqtc.get_ifdo_fields()[iFDOImageSetFieldName]['description']
        else:
            descr = iFDOImageSetFieldName
        self.info_text  = miqtwidgets.MyScrollbox(descr,height='50px')
        
        self._optional = optional
        
        self.checkNavFile.observe(self.checkNavFile_changed)
        self.checkSetValue.observe(self.checkSetValue_changed)

        validator = Validator(self.setValueCheck, float, self.setValue.value, empty_is_valid=empty_is_valid)
        self.setValue.observe(validator.handle_observe, names='value')

        self.checkNavFile.observe(on_change_fct)
        self.columnName.observe(on_change_fct)
        self.checkSetValue.observe(on_change_fct)
        self.setValue.observe(on_change_fct)
        self.checkInvert.observe(on_change_fct)

        #init
        self.checkSetValue.value = True
        self.checkNavFile.value = False
        self.checkSetValue.value = False
        # if valid const value found set field active
        if self.setValueCheck.valid == True:
            self.checkSetValue.value = True
        
        
    def getWidgets(self):
        return [self.fieldLabel,
               self.checkNavFile,
               self.columnName,
               widgets.HBox([miqtwidgets.HorizontalSpacer(1),self.checkInvert]),
               miqtwidgets.HorizontalSpacer(5),
               self.checkSetValue,
               self.setValueCheck,
               self.setValue,
               miqtwidgets.HorizontalSpacer(1),
               self.info_text]
    
    def checkNavFile_changed(self,b):
        self.columnName.disabled = not self.checkNavFile.value
        if not self._optional and self.checkNavFile.value == False and self.checkSetValue.value == False:
            self.checkSetValue.value = True

        self.checkInvert.disabled = self.columnName.disabled
        
    def checkSetValue_changed(self,b):
        self.setValue.disabled = not self.checkSetValue.value
        self.setValueCheck.disabled = not self.checkSetValue.value
        if not self._optional and self.checkNavFile.value == False and self.checkSetValue.value == False:
            self.checkNavFile.value = True

    def isValid(self): # TODO test
        if not self.setValueCheck.disabled and not self.setValueCheck.disabled.valid:
            return False
        return True

    def enable(self,enable_:bool):
        for item in self.getWidgets()[:-1]:
            item.disabled = not enable_
            if isinstance(item,widgets.Box):
                for subItem in item.children:
                    subItem.disabled = not enable_
        if enable_ == True:
            self.checkSetValue_changed(0)
            self.checkNavFile_changed(0)

    def invertFromNavFile(self):
        if isinstance(self.checkInvert,widgets.Checkbox) and not self.checkInvert.disabled and self.checkInvert.value:
            return True
        else:
            return False

class Point():
    def __init__(self,origin:np.array,point:np.array,name:str="",color='k'):
        self._origin = origin
        self._point = point
        self._vector = np.concatenate((origin, point), axis=None)
        self.name = name
        self.color = color

    @property
    def vector(self):
        return self._vector 

    @property
    def origin(self):
        return self._origin 

    @origin.setter
    def origin(self, value):
        self._origin = value
        self._vector = np.concatenate((self._origin, self._point), axis=None)

    @property
    def point(self):
        return self._point 

    @point.setter
    def point(self, value):
        self._point = value
        self._vector = np.concatenate((self._origin, self._point), axis=None)

    def setLabelToAx(self,ax):
        ax.text(self._origin[0]+self._point[0,0],self._origin[1]+self._point[1,0],self._origin[2]+self._point[2,0],  '%s' % (self.name), size=10, zorder=1, color=self.color)



class Tab_CoreItemsNavigation(TabBase):
    
    def __init__(self,tabsCommon:TabsCommon,iFDO,loadedHeaderFields,nav_file_start_dir:str):
        TabBase.__init__(self,tabsCommon)
        
        self.iFDO = iFDO
        
        # markdownd text, CAUTION may not be indented
        textWidget1 = miqtwidgets.MarkdownWidget("""
## Providing Core Information 

In order to create an iFDO file achieving FAIRness at least all the **core fields** should be provided.

### Navigation

In case you camera was stationary, i.e. all you images where taken at the same position and altitude, please provide spatial information as constant **Image-Set Values**.
Otherwise, please provide a navigation data file with the corresponding **Column Names** containing this information as a time series. The information per image is retrieved via 
linear interpolation and is written to an intermediate navigation file. Also both information can be provided, in that case the metadata for an individual image item always 
supersedes the corresponding metadata for the image-set. If **Image-Set Values** are not provided the values from the first item are automatically set as representative values for
the whole set.

In case the navigation's reference point does not coincide with the camera position the respective **Lever Arms** can be compensated for if the lever arms and the sensores attitude
are known. See section **Attitude** below.
            """)

        self.checkBoxOverrideIntNavFile = widgets.Checkbox(value=True,indent=False)
        self.checkBoxOverrideIntNavFile.observe(self.on_navFileOverride)
        self.navFileExistsWidget = widgets.HBox([ miqtwidgets.MyLabel("Intermediate Navigation file already exits. Overwrite:"),self.checkBoxOverrideIntNavFile])

        self.setButton.on_click(self.on_SetButton_clicked)
        self.notSetYetWarning = "" #"Values NOT set yet! Press 'Set' before you continue."
        self.setInfoLabel = widgets.Label(value = self.notSetYetWarning)
        setWidget = widgets.HBox([self.setButton,self.setInfoLabel])


        # nav data file
        self.navFileHeaders =[]
        self.navFileFC = miqtwidgets.FileChooserPaste(nav_file_start_dir)
        self.navFileFC._filename.observe(self.on_change_fct, names='value')
        self.navFileFC.register_callback(self.on_navFile_selected)
        self.navFileSeparator = widgets.Dropdown(options=[('Tab', "\t"), ('Space', " "), (",",","),(";",";")],
            value="\t",
        )
        self.navFileSeparator.observe(self.on_change_fct)
        self.navFileSeparator.observe(self.on_navFile_selected)
        self.timeFormat_format = widgets.Text(value=miqtv.date_formats['mariqt'],placeholder = "e.g: "+miqtv.date_formats['mariqt'])
        self.timeFormat_format.observe(self.on_change_fct)
        navFileitems = [miqtwidgets.MyLabel("Navigation Data File"),self.navFileFC.getWidget(),
                 miqtwidgets.MyLabel("Separator"),self.navFileSeparator,
                 miqtwidgets.MyLabel("DateTime Format"),self.timeFormat_format,]
        self.navFileParserWidget = widgets.GridBox(navFileitems, layout=widgets.Layout(width='100%',grid_template_columns='20% 79%'))
        
        # new field setter required
        items = []
        headerLine = [miqtwidgets.HorizontalSpacer(0)] * 10
        headerLine[2] = widgets.HTML(value = f"<b>Column Name</b>")
        headerLine[3] = widgets.HTML(value = f"<b>Invert</b>") 
        headerLine[7] = widgets.HTML(value = f"<b>Image-Set Value</b>")
        headerLine[9] = widgets.HTML(value = f"<b>Description</b>")
        items += headerLine
        self.latWidget = NavigationFieldWidget("Latitude",'image-latitude',loadedHeaderFields,self.on_change_fct,self.navFileHeaders)
        items += self.latWidget.getWidgets()
        self.lonWidget = NavigationFieldWidget("Longitude",'image-longitude',loadedHeaderFields,self.on_change_fct)
        items += self.lonWidget.getWidgets()
        self.altFieldWidget = NavigationFieldWidget("Altitude",'image-altitude-meters',loadedHeaderFields,self.on_change_fct,invertOption=True)
        items += self.altFieldWidget.getWidgets()
        self.coordUncertWidget = NavigationFieldWidget("Coordinate uncertainty",'image-coordinate-uncertainty-meters',loadedHeaderFields,self.on_change_fct)
        items += self.coordUncertWidget.getWidgets()
        self.metersAboveGroundWidget = NavigationFieldWidget("Meters above ground",'image-meters-above-ground',loadedHeaderFields,self.on_change_fct,optional=True,invertOption=True)
        items += self.metersAboveGroundWidget.getWidgets()

        # date time
        self.dateTimeColumnWidget = widgets.Dropdown(
            options=self.navFileHeaders,
            layout=widgets.Layout(width='100%')
        )
        self.dateTimeColumnWidget.observe(self.on_change_fct)
        dateTimeItems = [miqtwidgets.MyLabel("DateTime"),miqtwidgets.HorizontalSpacer(0),self.dateTimeColumnWidget,miqtwidgets.HorizontalSpacer(0),miqtwidgets.HorizontalSpacer(0),miqtwidgets.HorizontalSpacer(0),miqtwidgets.HorizontalSpacer(0),miqtwidgets.HorizontalSpacer(0),miqtwidgets.HorizontalSpacer(0),
                        miqtwidgets.MyScrollbox("in UTC",height='50px')]
        items += dateTimeItems
        self.fieldSetterWidget = widgets.GridBox(items, layout=widgets.Layout(width='100%',grid_template_columns= '18% 22px 20% 22px 5% 22px 22px 15% 2% auto')) #'18% 5% 20% 3% 5% 3% 15% 2% auto'))
        self.items = items

        # video update frequency
        self.videoUpdateFreq = widgets.BoundedFloatText(
            value=1,
            min=0.000,
            max=3600.0,
            step=0.1,
            layout = widgets.Layout(width='60px')
        )
        self.videoUpdateFreq.observe(self.on_change_fct)
        videoUpdateFreqItems = [miqtwidgets.MyLabel("Write navigation for videos every "),self.videoUpdateFreq,miqtwidgets.MyLabel("second(s)")]
        self.videoUpdateFreqWidget = widgets.HBox(videoUpdateFreqItems,layout=widgets.Layout(width='100%'))

        self.headerFieldWidgets = [self.latWidget,self.lonWidget,self.altFieldWidget,self.coordUncertWidget,self.metersAboveGroundWidget]

        self.navFileUsageObserve([e.checkNavFile for e in self.headerFieldWidgets],[dateTimeItems[0],dateTimeItems[2]] + navFileitems + videoUpdateFreqItems)
        
        self.checkNavFileExists()


        # optional attitude

        textWidget_attitude = miqtwidgets.MarkdownWidget("""
In addition to the camera's position, it's viewing direction (attitude) is valuable information. As usually rather the attitude of a frame or vehicle
holding the camera is recorded than the attitude of the camera itself, the latter can be derived if the attitude of the camera with respect to the 
frame is known. This section allows you to provide dynamic or static attitude information of the frame holding the camera as well as the static orientation
of the camera within that frame in order to determine the camera's absolute attitude.
<br/><br/>
Since three-dimensional rotations are not very intuitive and consecutive rotations are not commutative, care must be taken regarding the **order and direction
of rotations**. For the description of the **frame's attitude** the **Yaw, Pitch, Roll Convertion is expected** which describes the rotation of the frame's
coordinate system (x<sub>f</sub>-forward, y<sub>f</sub>-rightward, z<sub>f</sub>-downward)
which is initially aligned to a stationary NED-coordinate system (x<sub>NED</sub>-North, y<sub>NED</sub>-East, z<sub>NED</sub>-Down) and then rotated:

1. by angle **Yaw** around the downward pointing z<sub>f</sub>-axis, at `yaw=0` the frame faces North.
2. by angle **Pitch** around the rotated rigthward pointing y<sub>f</sub>-axis, at `pitch=0` the frame's forward axis is horizontally aligned with the planet's sphere surface
3. by angle **Roll** around the rotated forward pointing x<sub>f</sub>-axis, at `roll=0` the frame's rightward axis is horizontally aligned with the planet's sphere surface

The **positive rotation direction** around an axis can be determined by the *right-hand rule* (thumb points along axis, bent fingers indicate direction of 
positive rotation). Please **make sure** the data you provide complies with this convention!

The **camera's attitude** (x<sub>c</sub>-top, y<sub>c</sub>-right, z<sub>c</sub>-line-fo-sight) within the frame on the other hand
is to be described here by an optional **default orientation** followed by three consecutive rotations around the frame axes x<sub>f</sub>, y<sub>f</sub>, z<sub>f</sub>, respectively (see visualization bellow).
Double check with the visualization that it agrees in viewing direction *and* image orientation with the actual configuration.
            """)

        items = []
        headerLine = [miqtwidgets.HorizontalSpacer(0)] * 10
        headerLine[2] = widgets.HTML(value = f"<b>Column Name</b>")
        headerLine[3] = widgets.HTML(value = f"<b>Invert</b>") 
        headerLine[7] = widgets.HTML(value = f"<b>Constant Values</b>")
        headerLine[9] = widgets.HTML(value = f"<b>Description</b>")
        items += headerLine
        self.yawFrameWidget = NavigationFieldWidget("Frame Yaw",'Vehicle/Frame yaw angle in degrees',loadedHeaderFields,self.on_change_fct,
                                                    self.navFileHeaders,optional=False,invertOption=True,empty_is_valid=False)
        items += self.yawFrameWidget.getWidgets()
        self.pitchFrameWidget = NavigationFieldWidget("Frame Pitch",'Vehicle/Frame pitch angle in degrees',loadedHeaderFields,self.on_change_fct,
                                                      self.navFileHeaders,optional=False,invertOption=True,empty_is_valid=False)
        items += self.pitchFrameWidget.getWidgets()
        self.rollFrameWidget = NavigationFieldWidget("Frame Roll",'Vehicle/Frame roll angle in degrees',loadedHeaderFields,self.on_change_fct,
                                                     self.navFileHeaders,optional=False,invertOption=True,empty_is_valid=False)
        items += self.rollFrameWidget.getWidgets()

        self.navFileAttDegreeRadRadionButtons = widgets.RadioButtons(options=[('degrees',False), ('rad',True)])
        self.navFileAttDegreeRadRadionButtons.observe(self.on_change_fct)
        items += [miqtwidgets.HorizontalSpacer(0),miqtwidgets.HorizontalSpacer(0),self.navFileAttDegreeRadRadionButtons]
        self.yawFrameWidget.checkNavFile.observe(self.attNavFileCheckChanged)
        self.pitchFrameWidget.checkNavFile.observe(self.attNavFileCheckChanged)
        self.rollFrameWidget.checkNavFile.observe(self.attNavFileCheckChanged)


        self.attitudeFieldWidgets = [self.yawFrameWidget,self.pitchFrameWidget,self.rollFrameWidget]
        fieldSetterWidget_attitude = widgets.GridBox(items, layout=widgets.Layout(width='100%',grid_template_columns= '18% 22px 20% 22px 5% 22px 22px 15% 2% auto'))
        # default settings
        self.attDefaultDropdown = widgets.Dropdown(
            options=[   ('Bottom (top forw.)', [0,0,0]), 
                        ('Forward', [0,90,0]),
                        ('Backward', [180,90,0]),
                        ('Right', [90,90,0]),
                        ('Left', [-90,90,0])
                    ],
            layout=widgets.Layout(width='150px')
        )

        defaultSettingsBox = widgets.HBox([widgets.Label("Defaults:"),miqtwidgets.HorizontalSpacer(0), self.attDefaultDropdown],layout= widgets.Layout(margin='3px 0px 10px 0px'))

        items = []
        items += [widgets.HTML(value = markdown.markdown("""Additional rotaion around x<sub>f</sub>""") )]
        self.frame2camYaw_widget = widgets.FloatText(layout=widgets.Layout(width='100%'))
        self.frame2camYaw_widget.observe(self.on_change_fct)
        items += [self.frame2camYaw_widget,miqtwidgets.HorizontalSpacer(0)]
        items += [miqtwidgets.MyScrollbox('Additional rotation of the camera around the vehcile\'s x-axis in degrees',height='50px')]
        items += [widgets.HTML(value = markdown.markdown("""Additional rotaion around y<sub>f</sub>""") )]
        self.frame2camPitch_widget = widgets.FloatText(layout=widgets.Layout(width='100%'))
        self.frame2camPitch_widget.observe(self.on_change_fct)
        items += [self.frame2camPitch_widget,miqtwidgets.HorizontalSpacer(0)]
        items += [miqtwidgets.MyScrollbox('Additional rotation of the camera around the vehcile\'s y-axis in degrees',height='50px')]
        items += [widgets.HTML(value = markdown.markdown("""Additional rotaion around z<sub>f</sub>""") )]
        self.frame2camRoll_widget = widgets.FloatText(layout=widgets.Layout(width='100%'))
        self.frame2camRoll_widget.observe(self.on_change_fct)
        items += [self.frame2camRoll_widget,miqtwidgets.HorizontalSpacer(0)]
        items += [miqtwidgets.MyScrollbox('Additional rotation of the camera around the vehcile\'s z-axis in degrees',height='50px')]
        cam2FrameAdditionlRotGrid = widgets.GridBox(items, layout=widgets.Layout(width='100%',grid_template_columns= 'auto 15.5% 2.5% 32.5%'))
        cam2FrameWidgetsBox = widgets.VBox([widgets.HTML(value = f"<b>Camera Orientation in Frame</b>"),defaultSettingsBox,cam2FrameAdditionlRotGrid])

        cos_plot = widgets.interactive_output(self.update_cos_plot,{'rot_x':self.frame2camYaw_widget,'rot_y':self.frame2camPitch_widget,'rot_z':self.frame2camRoll_widget,'defaultOrientation':self.attDefaultDropdown})
        cos_plot.layout.height = '500px'
        # lots of white space left and right
        spaceLeft = -70
        spaceRight = -70
        cos_plot.add_class("left-spacing-class-" + str(spaceLeft))
        # TODO
        # if spaceLeft not in existingSpacingClasses_left:
        #     display(widgets.HTML("<style>.left-spacing-class-" + str(spaceLeft) + " {margin-left: " + str(spaceLeft) + "px;}</style>"))
        #     existingSpacingClasses_left.append(spaceRight)
        cos_plot.add_class("right-spacing-class-" + str(spaceRight))
        # TODO
        # if spaceRight not in existingSpacingClasses_right:
        #     display(widgets.HTML("<style>.right-spacing-class-" + str(spaceRight) + " {margin-right: " + str(spaceRight) + "px;}</style>"))
        #     existingSpacingClasses_right.append(spaceRight)

        cosPlotDescr = miqtwidgets.MyScrollbox("Illustration of the camera orientation within the vehicle frame. The orientation is a combination of the default orientation plus three consecutive rotations:\n \
            1. rotation around frame x-axis \n 2. rotation around frame y-axis \n 3. rotation around frame z-axis",height = '200px')
        
        cos_plot_box = widgets.GridBox([cos_plot,widgets.VBox([miqtwidgets.VerticalSpacer(40), cosPlotDescr])],layout=widgets.Layout(width='100%',grid_template_columns= '67% 32.5%'))

        # position lever arm compensation
        textWidget_leverarms = miqtwidgets.MarkdownWidget("""
The vehicle's attitude data can also be used to compensate for an offset between the imported positions' reference point and the camera position within the vehicle. Please provide those offsets in vehicle coordinates in meters.
            """)
        self.offest_x_widget = widgets.FloatText(description="Offest x",layout=widgets.Layout(width='200px'))
        self.offest_y_widget = widgets.FloatText(description="Offest y",layout=widgets.Layout(width='200px'))
        self.offest_z_widget = widgets.FloatText(description="Offest z",layout=widgets.Layout(width='200px'))
        self.offest_x_widget.observe(self.on_change_fct)
        self.offest_y_widget.observe(self.on_change_fct)
        self.offest_z_widget.observe(self.on_change_fct)
        leverarmsWidgetsBox = widgets.VBox([widgets.HTML(value = f"<b>Position Lever Arm Compensation</b>"),
                                            textWidget_leverarms,
                                            self.offest_x_widget,
                                            self.offest_y_widget,
                                            self.offest_z_widget
                                            ])

        self.attitude_accordion = widgets.Accordion(children=[widgets.VBox([textWidget_attitude,
                                                                            miqtwidgets.VerticalSpacer(0),
                                                                            fieldSetterWidget_attitude,
                                                                            miqtwidgets.VerticalSpacer(0),
                                                                            cam2FrameWidgetsBox,
                                                                            cos_plot_box,
                                                                            leverarmsWidgetsBox],)], selected_index=None)
        #self.attitude_accordion.set_title(0, 'Attitude (Optional)')
        self.attitude_accordion.layout.width = '100%'
        self.attitude_accordion.observe(self.on_change_fct)
        self.attitude_accordion.observe(self.on_attitude_accordion_folded)
        self.on_attitude_accordion_folded("foo")

        self.NavigationTabOutput = widgets.Output()
        self.myWidget = widgets.VBox([textWidget1,
                                      miqtwidgets.VerticalSpacer(30),
                                      self.navFileExistsWidget,
                                      self.navFileParserWidget,
                                      miqtwidgets.VerticalSpacer(30),
                                      widgets.HBox([miqtwidgets.HorizontalSpacer(40), self.fieldSetterWidget]),
                                      miqtwidgets.VerticalSpacer(0),
                                      widgets.HBox([miqtwidgets.HorizontalSpacer(40), self.videoUpdateFreqWidget]),
                                      miqtwidgets.VerticalSpacer(30),
                                      widgets.HBox([miqtwidgets.HorizontalSpacer(26), self.attitude_accordion]),
                                      miqtwidgets.VerticalSpacer(30),
                                      setWidget,
                                      self.outputWidget,
                                      self.NavigationTabOutput,
                                      miqtwidgets.VerticalSpacer(30),
                                      self.nextTabButton])
  
    def navFileUsageObserve(self,toBeObersverd:list,toBeActedOn:list):

        self.toBeObersverd = toBeObersverd
        self.toBeActedOn = toBeActedOn

        for item in toBeObersverd:
            item.observe(self.navFileUsage_changed)

    def attNavFileCheckChanged(self,b):
        if self.yawFrameWidget.checkNavFile.value or self.pitchFrameWidget.checkNavFile.value or self.rollFrameWidget.checkNavFile.value:
            self.navFileAttDegreeRadRadionButtons.disabled = False
        else:
            self.navFileAttDegreeRadRadionButtons.disabled = True

    def navFileUsage_changed(self,b):
        enable = True
        i = 0
        for item in self.toBeObersverd:
            if item.value == False or item.disabled:
                i +=1
        if i == len(self.toBeObersverd):
            enable = False
        for item in self.toBeActedOn:
            item.disabled = not enable

    def checkNavFileExists(self):
        for item in self.navFileExistsWidget.children:
            item.disabled = not self.iFDO.intermediateNavFileExists()

        if self.iFDO.intermediateNavFileExists() and self.navFileExistsWidget.layout.visibility == 'hidden':
            self.navFileExistsWidget.layout.visibility = 'visible'
            self.checkBoxOverrideIntNavFile.disabled = False
            self.checkBoxOverrideIntNavFile.value = True
        if not self.iFDO.intermediateNavFileExists():
            self.navFileExistsWidget.layout.visibility = 'hidden'
            self.checkBoxOverrideIntNavFile.disabled = True
            self.checkBoxOverrideIntNavFile.value = True

    def on_attitude_accordion_folded(self,b):
        # dont allow to to fold. Not nice! but accordion cant be disabeld :(
        if not self.checkBoxOverrideIntNavFile.value:
           self.attitude_accordion.selected_index = None 
        # set title
        if self.attitude_accordion.selected_index != None:
            self.attitude_accordion.set_title(0, 'Attitude (Optional) - Enabled')
        else:
            self.attitude_accordion.set_title(0, 'Attitude (Optional) - Disabled')
    
    def on_navFileOverride(self,b):
        if self.checkBoxOverrideIntNavFile.value:
            for item in self.headerFieldWidgets:
                item.optional = False
                item.checkSetValue.disabled = False
                item.checkNavFile.disabled = False # hidden depth/alt not!
            self.navFileUsage_changed(0)
        else:
            for item in self.headerFieldWidgets:
                item.optional = True
                item.checkNavFile.disabled = True
                item.columnName.disabled = True
                item.checkInvert.disabled = True
                item.checkSetValue.disabled = True
                item.setValue.disabled = True
                item.setValueCheck.disabled = True
            # attitude fold
            self.attitude_accordion.selected_index = None

    def on_navFile_selected(self,b):
        #with miqtwidgets.Capturing() as output:       

        if self.navFileFC.selected == None:
            return
        with open(self.navFileFC.selected,'r') as f:
            separator = self.navFileSeparator.value
            first_line = f.readline().strip()
            self.navFileHeaders = first_line.split(separator)
        
        one_active = False
        for item in self.headerFieldWidgets + self.attitudeFieldWidgets:
            item.columnName.options = self.navFileHeaders
            # select last part of field label for matching if there is a space (e.g. Frame Yaw)
            label = item.fieldLabel.myvalue
            try:
                if 'pitch' in label.lower() or 'roll' in label.lower():
                    label = item.fieldLabel.myvalue.split(" ")[-1][0:4]
                else:
                    label = item.fieldLabel.myvalue.split(" ")[-1]#[0:3]
                    label = label.lower()
                    label = label.replace('altitude','depth') # get column depth as alititude
                    label = label.replace('ground','altitude') # get column alitude as meters above ground
            except Exception as ex:
                pass
            
            
            lower_case_options = [e.lower() for e in self.navFileHeaders]
            original_options_dict = {}
            for opt in self.navFileHeaders:
                original_options_dict[opt.lower()] = opt

            matches = difflib.get_close_matches(label,lower_case_options)
            if len(matches) != 0:
                new_val = original_options_dict[matches[0]]
                item.columnName.value = new_val
                item.checkNavFile.value = True
                one_active = True
            else:
                # to make sure at least one is active, otherwise everthing is disabled
                if one_active:
                    item.checkNavFile.value = False
                else:
                    item.columnName.value = item.columnName.options[0]
                    item.checkNavFile.value = True
                    one_active = True
            
        self.dateTimeColumnWidget.options = self.navFileHeaders
        try:
            self.dateTimeColumnWidget.value = difflib.get_close_matches("Time",self.navFileHeaders)[0]
        except IndexError as ex:
                pass
                
        #debugOutputWidget.addText(str(output))


    def on_SetButton_clicked(self,b):
        with self.NavigationTabOutput:
    
            attitudeDataProvided = False
            if self.attitude_accordion.selected_index != None:
                attitudeDataProvided = True

            navigation_file = self.navFileFC.selected
            if navigation_file == None:
                navigation_file = ""
            date_format = self.timeFormat_format.value


            # attitude ##############################################
            msg_att_1 = ""
            msg_att_2 = ""
            success_att = True
            allConstFieldFilled = False
            frame_att_header = {}
            if attitudeDataProvided:
                [yaw,pitch,roll] = miqtg.yawPitchRoll(self.R)
                # check const fields
                allConstFieldFilled = True
                navFileUsed = False
                for item in self.attitudeFieldWidgets:
                    if item.checkSetValue.value and not item.checkSetValue.disabled:
                        if not item.setValueCheck.valid:
                            msg_att_1 += "Invalid field: " + item.fieldLabel.myvalue+"\n"
                            success_att = False
                    else:
                        allConstFieldFilled = False
                    if item.checkNavFile.value == True and not item.checkNavFile.disabled:
                        navFileUsed = True
                # set header fields if all yaw,pitch,roll const fields set (all three required for calculation) 
                if allConstFieldFilled:
                    try:
                        self.iFDO.set_image_set_attitude(   float(self.yawFrameWidget.setValue.value),
                                                            float(self.pitchFrameWidget.setValue.value),
                                                            float(self.rollFrameWidget.setValue.value),
                                                            yaw,
                                                            pitch,
                                                            roll)                                                               
                    except Exception as ex:
                        msg_att_1 += str(ex.args)+"\n"
                    

                # set item fields
                if msg_att_1 == "" and navFileUsed:
                    const_att_values = {}
                    if self.yawFrameWidget.checkSetValue.value and not self.yawFrameWidget.checkSetValue.disabled:
                        const_att_values['yaw'] = self.yawFrameWidget.setValue.value
                    if self.pitchFrameWidget.checkSetValue.value and not self.pitchFrameWidget.checkSetValue.disabled:
                        const_att_values['pitch'] = self.pitchFrameWidget.setValue.value
                    if self.rollFrameWidget.checkSetValue.value and not self.rollFrameWidget.checkSetValue.disabled:
                        const_att_values['roll'] = self.rollFrameWidget.setValue.value

                    records2beInverted = []
                    frame_att_header = {'utc':	self.dateTimeColumnWidget.value}
                    if self.yawFrameWidget.checkNavFile.value == True and not self.yawFrameWidget.checkNavFile.disabled:
                        frame_att_header['yaw'] =	self.yawFrameWidget.columnName.value
                        if self.yawFrameWidget.invertFromNavFile():
                            records2beInverted.append('yaw')
                    if self.pitchFrameWidget.checkNavFile.value == True and not self.pitchFrameWidget.checkNavFile.disabled:
                        frame_att_header['pitch'] =	self.pitchFrameWidget.columnName.value
                        if self.pitchFrameWidget.invertFromNavFile():
                            records2beInverted.append('pitch')
                    if self.rollFrameWidget.checkNavFile.value == True and not self.rollFrameWidget.checkNavFile.disabled:
                        frame_att_header['roll'] =	self.rollFrameWidget.columnName.value
                        if self.rollFrameWidget.invertFromNavFile():
                            records2beInverted.append('roll')

                    try:
                        success_att, msg_att_2 = self.iFDO.create_image_attitude_file(navigation_file, frame_att_header, yaw, pitch, roll,
                                                        date_format, const_values = const_att_values, overwrite=self.checkBoxOverrideIntNavFile.value, col_separator=self.navFileSeparator.value,
                                                        att_path_angles_in_rad=self.navFileAttDegreeRadRadionButtons.value,
                                                        videoSampleSeconds=self.videoUpdateFreq.value,
                                                        records2beInverted = records2beInverted)
                    except Exception as ex:
                        msg_att_2 = str(ex.args) + msg_att_2



            # position ##############################################

            # header ####################
            msg1 = ""
            header_update = {}
        
            headersUsed = False
            navFileUsed = False
            for item in self.headerFieldWidgets:
                if item.checkSetValue.value and not item.checkSetValue.disabled:
                    headersUsed = True
                    if item.setValueCheck.valid:
                        if item.setValue.value == "":
                            val = item.setValue.value
                        else:
                            val = float(item.setValue.value)
                        header_update[item.iFDOImageSetFieldName] = val
                    else:
                        msg1 += "Invalid field: " + item.fieldLabel.myvalue +"\n"
                if item.checkNavFile.value == True and not item.checkNavFile.disabled:
                    navFileUsed = True

            try:
                self.iFDO.update_ifdo_header_fields(header_update)
            except Exception as ex:
                msg1 += str(ex.args)+"\n"
            
            
            # items #####################
            success2 = True
            msg2 = ""
            records2beInverted = []
            if navFileUsed:
                nav_header = {'utc':	self.dateTimeColumnWidget.value}
                if self.latWidget.checkNavFile.value == True and not self.latWidget.checkNavFile.disabled:
                    nav_header['lat'] =	self.latWidget.columnName.value
                    if self.latWidget.invertFromNavFile():
                        records2beInverted.append('lat')
                if self.lonWidget.checkNavFile.value == True and not self.lonWidget.checkNavFile.disabled:
                    nav_header['lon'] =	self.lonWidget.columnName.value
                    if self.lonWidget.invertFromNavFile():
                        records2beInverted.append('lon')
                if self.coordUncertWidget.checkNavFile.value == True and not self.coordUncertWidget.checkNavFile.disabled:
                    nav_header['uncert'] =	self.coordUncertWidget.columnName.value
                    if self.coordUncertWidget.invertFromNavFile():
                        records2beInverted.append('uncert')
                if self.altFieldWidget.checkNavFile.value == True and not self.altFieldWidget.checkNavFile.disabled:
                    nav_header['alt'] = self.altFieldWidget.columnName.value
                    if self.altFieldWidget.invertFromNavFile():
                        records2beInverted.append('alt')
                if self.metersAboveGroundWidget.checkNavFile.value == True and not self.metersAboveGroundWidget.checkNavFile.disabled:
                    nav_header['hgt'] = self.metersAboveGroundWidget.columnName.value
                    if self.metersAboveGroundWidget.invertFromNavFile():
                        records2beInverted.append('hgt')
                if attitudeDataProvided:
                    nav_header = {**nav_header,**frame_att_header}
                    # TODO does not work with const values yet
                    #if not 'yaw' in frame_att_header:
                    #    nav_header['yaw'] = const_att_values['yaw']
                    #if not 'pitch' in frame_att_header:
                    #    nav_header['pitch'] = const_att_values['pitch']
                    #if not 'roll' in frame_att_header:
                    #    nav_header['roll'] = const_att_values['roll']

                if self.dateTimeColumnWidget.value is None:
                    msg1 += "Error: DateTime column not selected"
                else:
                    try:
                        success2 = False
                        success2, msg2 = self.iFDO.create_image_navigation_file(navigation_file,
                                                                                nav_header,date_format,
                                                                                overwrite=self.checkBoxOverrideIntNavFile.value,
                                                                                col_separator=self.navFileSeparator.value,
                                                                                videoSampleSeconds=self.videoUpdateFreq.value,
                                                                                offset_x=self.offest_x_widget.value,
                                                                                offset_y=self.offest_y_widget.value,
                                                                                offset_z=self.offest_z_widget.value,
                                                                                angles_in_rad=self.navFileAttDegreeRadRadionButtons.value,
                                                                                records2beInverted = records2beInverted)
                        msg2 += "\n"
                    except Exception as ex:
                        msg2 = str(ex.args) + msg2 + "\n"
                
            
            if msg1 == "" and success2:
                success = True
            else:
                success = False
            
            if msg1 == "" and headersUsed:
                msg1 = "Navigation header values set.\n"


            

            
            if msg_att_1 == "" and allConstFieldFilled:
                msg_att_1 = "Attitude header values set.\n"

                
            self.checkNavFileExists()

            self.writeToOutputWidget(str(msg1) + str(msg2) + msg_att_1 + msg_att_2)
            
            if success and success_att:
                self.setInfoLabel.value = ""
                self.tabValidate(True)
                
        #debugOutputWidget.addText(str(output))      

    def update_cos_plot(self,rot_x,rot_y,rot_z,defaultOrientation):

        R_defaultAngles = miqtg.R_YawPitchRoll(defaultOrientation[0],defaultOrientation[1],defaultOrientation[2])
        R_additional = miqtg.R_XYZ(rot_x,rot_y,rot_z)
        R = R_additional.dot(R_defaultAngles)
        self.R = R

        # vehicle kos
        origin = np.array([0, 0, 0,])
        x1_0 = Point(origin,np.array([[1], [0], [0]]),"")
        y1_0 = Point(origin,np.array([[0], [1], [0]]),"")
        z1_0 = Point(origin,np.array([[0], [0], [1]]),"")
        kos1_0 = np.row_stack([x1_0.vector, y1_0.vector, z1_0.vector])
        x1 = Point(np.array([.5, 0, 0]),np.array([[1], [0], [0]]),"  $x_{f}$ forw")
        y1 = Point(np.array([0, .5, 0]),np.array([[0], [1], [0]]),"  $y_{f}$ right")
        z1 = Point(np.array([0, 0, .5]),np.array([[0], [0], [1]]),"  $z_{f}$ down")
        kos1 = np.row_stack([x1.vector, y1.vector, z1.vector])

        # cam kos default
        x2_ = Point(origin,np.array([[1], [0], [0]]),"")
        y2_ = Point(origin,np.array([[0], [1], [0]]),"")
        z2_ = Point(origin,np.array([[0], [0], [1]]),"")
        # cam kos rotated
        x2 = Point(origin,R.dot(x2_.point),"  $x_{c}$ top",color='g')
        y2 = Point(origin,R.dot(y2_.point),"  $y_{c}$ right",color='g')
        z2 = Point(origin,R.dot(z2_.point),"  $z_{c}$ line of sight",color='g')
        kos2 = np.row_stack([x2.vector,y2.vector,z2.vector])

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        X, Y, Z, U, V, W = zip(*kos1_0)
        ax.quiver(X, Y, Z, U, V, W, color=x1.color,arrow_length_ratio=0)
        x1_0.setLabelToAx(ax)
        y1_0.setLabelToAx(ax)
        z1_0.setLabelToAx(ax)

        X, Y, Z, U, V, W = zip(*kos1)
        ax.quiver(X, Y, Z, U, V, W, color=x1.color,arrow_length_ratio=0.2)
        x1.setLabelToAx(ax)
        y1.setLabelToAx(ax)
        z1.setLabelToAx(ax)

        X, Y, Z, U, V, W = zip(*kos2)
        ax.quiver(X, Y, Z, U, V, W, color=y2.color,arrow_length_ratio=0.2)
        x2.setLabelToAx(ax)
        y2.setLabelToAx(ax)
        z2.setLabelToAx(ax)

        lim = [-1.0, 1.0]
        ax.set_xlim(lim)
        ax.set_ylim(lim)
        ax.set_zlim(lim)

        plt.gca().invert_zaxis()
        plt.gca().invert_yaxis()
        plt.axis('off')

        #legend
        handles, labels = plt.gca().get_legend_handles_labels()
        line1 = Line2D([0], [0], label='Vehicle/Frame', color=x1.color)
        line2 = Line2D([0], [0], label='Camera', color=x2.color)

        handles.extend([line1,line2])

        plt.legend(handles=handles,loc="upper left")

        fig.canvas.toolbar_visible = False
        fig.canvas.header_visible = False
        fig.canvas.footer_visible = False
        fig.canvas.resizable = False
        plt.show()


    def on_checkButton_clicked(self,b):
        self.tabValidate(True)
        
    def getWidget(self):
        return self.myWidget
    
    def getTitle(self):
        return "Navigation"
    
    def on_change_fct(self,change=None):
        self.writeToOutputWidget("")
        self.tabValidate(False)



    
##### TAB: Create Core Fields ################################
    
    
class Tab_createCoreFields(TabBase):
    
    def __init__(self,tabsCommon:TabsCommon,iFDO):
        TabBase.__init__(self,tabsCommon)
        
        # markdownd text, CAUTION may not be indented
        textWidget = miqtwidgets.MarkdownWidget("""

Let's check if all the necessary Core Information is there:


            """)
        
        createCoreFieldsButton = widgets.Button(description = "Create Core iFDO Fields",layout=widgets.Layout(width='auto'))

        self.output = widgets.Output()

        def on_createCoreFieldsButton_click(b):
            self.output.clear_output()
            self.writeToOutputWidget("")
            with self.output:
                try:
                    msg = []
                    print("Creating intermediate start time file")
                    msg.append("Create intermediate start time file:\n" + str(iFDO.create_start_time_file()))
                    print("Creating intermediate hash file")
                    msg.append("Create intermediate image hash file:\n" + str(iFDO.create_image_sha256_file(reReadAll=False)))
                    msg.append("\nCreate core fields:")
                    tryMsg = ""

                    #with miqtwidgets.Capturing() as output:
                    print("Creating Core Fields")
                    #iFDO.createCoreFields()
                    iFDO.update_fields()
                    #msg += output
                    tryMsg ="All required core fields successfully created."
                    self.tabValidate(True)

                except Exception as ex:
                    self.tabValidate(False)
                    tryMsg =str(ex.args).replace("\\n","\n")

            msg.append(tryMsg)
            self.writeToOutputWidget("\n".join(msg))

        createCoreFieldsButton.on_click(on_createCoreFieldsButton_click)        
        
        self.myWidget = widgets.VBox([textWidget,
                                      widgets.HBox([createCoreFieldsButton,widgets.Label()]),
                                      self.output,
                                      self.outputWidget,
                                      miqtwidgets.VerticalSpacer(30),
                                      self.nextTabButton])
        
        
    def getWidget(self):
        return self.myWidget
    
    def getTitle(self):
        return "Create Core Fields"
    
    def on_change_fct(self):
        self.tabValidate(False)
        self.writeToOutputWidget("")





    
##### TAB: Caputure & Content Fields ################################
    
    
class Tab_capterContentFields(TabBase):
    
    def __init__(self,tabsCommon:TabsCommon,iFDO,loadedHeaderFields,parseFolderButtonOutput):
        TabBase.__init__(self,tabsCommon)
        
        self.parseFolderButtonOutput = parseFolderButtonOutput
        # set button
        self.outputCustomSetButton = widgets.Output()
        #setCustomButton = widgets.Button(description="Set")
        self.notSetYetWarning = "" #"Values NOT set yet! Press 'Set' before you continue."
        self.setCustomInfoLabel = widgets.Label(value = self.notSetYetWarning)
        setCustomWidget = widgets.HBox([self.setButton,self.setCustomInfoLabel])

        self.setCustomMsgWidget = widgets.HTML()

        self.iFDO = iFDO
        self.loadedHeaderFields = loadedHeaderFields

        
        # markdownd text, CAUTION may not be indented
        textWidget = miqtwidgets.MarkdownWidget("""

## Providing Capture and Content Information

This information is not strictly required but will certainly improve you iFDO's quality. Try to provide what you can, the more information the better!
            """)
        
        captureHaederHeadingWidget = miqtwidgets.MarkdownWidget("""
## Capture and Content Header Fields
            """)
        
        header_captureFields = {}
        for field in get_but_min_header_fields():
            useField = True
            for entry in EXCLUDE_FROM_HEADER_FIELDS:
                if entry in field:
                    useField = False
                    break
            if useField:
                header_captureFields[field] = get_but_min_header_fields()[field]

        self.gridWidgetCreator_captureFields = GridFieldWidgetCreator(header_captureFields,loadedHeaderFields,self.on_change_fct,optional=True)
        gridWidget_captureFields = self.gridWidgetCreator_captureFields.getWidget()

        captureItemsHeadingWidget = miqtwidgets.MarkdownWidget("""
## Capture and Content Item Fields

Item fields can be loaded from auxiliary text files which contain a column with the image file names (without the path) and a column per item field. In case multiple item field values per **video** file are provided an additional column cotaining the respective time stamp in **UTC** is required.  
            """)
        
        acquiOutputWidget = widgets.Output() #HTML()


        class HeaderFieldWidget(widgets.VBox):
            """ VBox widget containing a widget for the iFDO item field name and the respective column name in a file to parse from """
            def __init__(self,columnOptions:list,fieldOptions:list,on_change_fct):

                self.comboBox_field = widgets.Combobox(options=fieldOptions, placeholder="Field Name",layout=widgets.Layout(width='98%'))
                self.dropdown_columnName = widgets.Dropdown(options=columnOptions,layout=widgets.Layout(width='98%'))
                if not isinstance(on_change_fct,list):
                    on_change_fct = [on_change_fct]
                for fkt in on_change_fct:
                    self.comboBox_field.observe(fkt,names='value')
                    self.dropdown_columnName.observe(fkt,names='value')
                    
                widgets.VBox.__init__(self,[self.dropdown_columnName,self.comboBox_field],layout=widgets.Layout(width='auto',overflow_x='hidden',))

            def __eq__(self,other):
                if other.comboBox_field.options == self.comboBox_field.options and \
                    other.comboBox_field.value == self.comboBox_field.value and \
                    other.dropdown_columnName.options == self.dropdown_columnName.options and \
                    other.dropdown_columnName.value == self.dropdown_columnName.value:
                    return True
                return False

            def getColumnName(self):
                return self.dropdown_columnName.value

            def getFieldName(self):
                return self.comboBox_field.value

            def setFieldName(self,name:str):
                self.comboBox_field.value = name

            def setColumnName(self,name:str):
                try:
                    self.dropdown_columnName.value = name
                except Exception:
                    raise Exception("Invalid selection.",name,"not in",self.dropdown_columnName.options)

            def setColumnOptions(self,options:list):
                self.dropdown_columnName.options = options

        itemWidgetExample =  miqtwidgets.FileParserWidget({**get_but_min_header_fields(),**{'image-filename':""}},self.on_change_fct,requiredFields="image-filename",iFDO=iFDO,allowConvert=False)
        self.editalbleListWidget_auxFilesCapture = miqtwidgets.EditalbleListWidget("Auxiliary Files:",itemWidgetExample,[])
        

        # create  acquisition auxiliary file
        createAcquiButton = widgets.Button(description="Create", layout=widgets.Layout(width='auto'))
        createAcquiButton.style.button_color = '#87CEFA'
        createAcquiLabel = widgets.Label("image acquisition settings auxiliary file with image exif header content.")
        createAcquiBox = widgets.HBox([createAcquiButton, createAcquiLabel])
        def on_createAcquiButton_clicked(b):
            with acquiOutputWidget:
                try:
                    success,msg = iFDO.createAcquisitionSettingsEXIFFile(override = True)
                except Exception as ex:
                    success = False
                    msg = ex.args
                
                print(msg)
                if not success:
                    return
                              
                element = iFDO.nonCoreFieldIntermediateItemInfoFiles[-1]
                header = {}
                for field in element.header:
                    header[field] = {'column-name':element.header[field], 'converter':{}}
                self.editalbleListWidget_auxFilesCapture.on_addButton_clicked(0, [element.fileName,element.separator,header])

                      
        createAcquiButton.on_click(on_createAcquiButton_clicked)
        
        
        customHeadingWidget = miqtwidgets.MarkdownWidget("""
## Custom Header Fields
            """)
        
        # find non standard header filds in current iFDO
        self.setCurrent_nonStandard_headerFields()
        
        def on_setButton_clicked(b):
            self.outputCustomSetButton.clear_output(wait = True)
            with self.outputCustomSetButton:
                self.tabValidate(False)
                self.setCustomInfoLabel.value = ""

                removedFields = []
                changedFields = {}
                # removed items
                updated_nonStandard_headerFields_dict = copy.deepcopy(self.currentiFDO_nonStandard_headerFields_dict)
                for dictItem in updated_nonStandard_headerFields_dict:
                    if dictItem not in [e.itemWidget.getParams()[0] for e in self.nonStandardHeaderFieldListWidget.itemObjList]:
                        updated_nonStandard_headerFields_dict[dictItem] = ""
                        removedFields.append(dictItem)


                # added items
                for listItem in self.nonStandardHeaderFieldListWidget.itemObjList:
                    fieldName = listItem.itemWidget.getParams()[0]
                    fieldValue = listItem.itemWidget.getParams()[1]
                    if fieldName != "":
                        try:
                            val = ast.literal_eval(fieldValue.strip())
                        except Exception:
                            val = fieldValue
                        tmpDict = {fieldName : val}
                        if not (fieldName in updated_nonStandard_headerFields_dict and fieldValue == updated_nonStandard_headerFields_dict[fieldName]):
                            updated_nonStandard_headerFields_dict[fieldName] = val
                            changedFields.update(tmpDict)
                        #if fieldValue == "":
                        #    removedFields.append(fieldName)

                
                msg = ""
                
                
                # update header fields
                try:
                    header_update = self.gridWidgetCreator_captureFields.getFieldsDict()
                except miqtc.IfdoException as e:
                    msg = str(e.args[0])

                if msg == "":
                    try:
                        header_update.update(updated_nonStandard_headerFields_dict)
                    except:
                        pass

                    try:
                        iFDO.update_ifdo_header_fields(header_update)
                    except Exception as ex:
                        msg += str(ex.args)
                    
                    
                    # load aux files
                    try:
                        auxFileInfoList = self.editalbleListWidget_auxFilesCapture.itemObjList
                    except NameError:
                        auxFileInfoList = []
                    try:
                        iFDO.nonCoreFieldIntermediateItemInfoFiles = [] # reset so really only the ones shown in gui are there
                        for file in auxFileInfoList:
                            fileName = file.itemWidget.getParams()[0]
                            separator = file.itemWidget.getParams()[1]
                            header = file.itemWidget.getParams()[2]
                            # no so nice work around
                            headerNoConverter = {}
                            for i in header:
                                headerNoConverter[i] = header[i]['column-name']
                            iFDO.add_item_info_tab_file(fileName,separator,headerNoConverter)
                    except Exception as ex:
                        msg += str(ex.args)
                    
                if msg == "":
                    msg = "Values set." # this way it appears that the message regards all fields
                    self.tabValidate(True)
                    
                self.setCustomMsgWidget.value = miqtwidgets.formatHTML(msg)
                

        self.setButton.on_click(on_setButton_clicked)

        currentiFDO_nonStandard_headerFields_list = self.currentiFDO_nonStandard_headerFields_list # dirty dirty
        class NonStandardHeaderFieldWidget(miqtwidgets.ItemWidgetBase):

            def __init__(self,on_change_fct,parseFolderButtonOutput):
                miqtwidgets.ItemWidgetBase.__init__(self,on_change_fct)
                self.parseFolderButtonOutput = parseFolderButtonOutput
                self.fieldNamePrefixWidget = widgets.Text(value = "image-",layout=widgets.Layout(width='90px'), disabled=True)
                self.fieldNameSuffixWidget = widgets.Text(value="Empty",layout=widgets.Layout(width='auto'))
                self.fieldNameSuffixWidget.observe(on_change_fct,names='value')
                self.fieldNameBox = widgets.HBox([self.fieldNamePrefixWidget,self.fieldNameSuffixWidget])
                self.fieldValueWidget = widgets.Text(value="Empty",layout=widgets.Layout(width='auto'))
                self.fieldValueWidget.observe(on_change_fct,names='value')
                self.widget = widgets.GridBox([widgets.Label("Field Name:"),widgets.Label("Field Value:"),
                                              self.fieldNameBox,self.fieldValueWidget], layout=widgets.Layout(width='100%',grid_template_columns='30% 69%'))

            def copy(self):
                ret = NonStandardHeaderFieldWidget(self.on_change_fct,self.parseFolderButtonOutput)
                ret.setParams(self.getParams())
                return ret

            def setParams(self,params=["image-",""]):
                # params = [name,value]
                if len(params) == 0:
                    params=[self.fieldNamePrefixWidget.value,""]
                if params[0][0:len(self.fieldNamePrefixWidget.value)] != self.fieldNamePrefixWidget.value:
                    with self.parseFolderButtonOutput:
                        print("Invalid field name: \"" + params[0] + "\". Must start with: " + self.fieldNamePrefixWidget.value + ". Is renamed to " + "\"image-" + params[0] + "\"")
                    params[0] = "image-" + params[0]
                self.fieldNameSuffixWidget.value = params[0][len(self.fieldNamePrefixWidget.value)::]
                self.fieldValueWidget.value = str(params[1])

            def getParams(self):
                return [self.fieldNamePrefixWidget.value + self.fieldNameSuffixWidget.value,self.fieldValueWidget.value]

            def getWidget(self):
                return self.widget

            def removeFromSource(self,params):
                try:
                    params[1] = ast.literal_eval(params[1].strip())
                except:
                    pass
                if params in currentiFDO_nonStandard_headerFields_list:
                    currentiFDO_nonStandard_headerFields_list.remove(params)
                    #currentiFDO_nonStandard_headerFields_dict[params[0]] = ""

            def readParamsFromElement(self,element):
                return element


        itemWidgetExample = NonStandardHeaderFieldWidget(self.on_change_fct,self.parseFolderButtonOutput)
        self.nonStandardHeaderFieldListWidget = miqtwidgets.EditalbleListWidget("Custom Header Fields",itemWidgetExample,self.currentiFDO_nonStandard_headerFields_list)
              
        self.myWidget = widgets.VBox([textWidget,
                                      miqtwidgets.VerticalSpacer(10),
                                      captureHaederHeadingWidget,
                                      gridWidget_captureFields,
                                      miqtwidgets.VerticalSpacer(10),
                                      
                                      captureItemsHeadingWidget,
                                      miqtwidgets.VerticalSpacer(10),
                                      createAcquiBox,
                                      acquiOutputWidget,
                                      miqtwidgets.VerticalSpacer(10),
                                      self.editalbleListWidget_auxFilesCapture.completeWidget,
                                      miqtwidgets.VerticalSpacer(10),
                                      
                                      customHeadingWidget,
                                      self.nonStandardHeaderFieldListWidget.completeWidget,
                                      miqtwidgets.VerticalSpacer(10),
                                      setCustomWidget,
                                      self.outputCustomSetButton,
                                      self.setCustomMsgWidget,
                                      miqtwidgets.VerticalSpacer(10),
                                                                            
                                      self.nextTabButton])
        
    def _onTabSelected(self):
        # load existing (e.g. attitude) # TODO split iFDO.nonCoreFieldIntermediateItemInfoFiles in capture and content to load them here on the correct capture/content area (so far only attitude)
        for item in self.iFDO.nonCoreFieldIntermediateItemInfoFiles:
            header = {}
            for field in item.header:
                header[field] = {'column-name':item.header[field], 'converter':{}}
            #self.editalbleListWidget_auxFilesCapture.on_addButton_clicked(0, [item.fileName,item.separator,item.header])
            self.editalbleListWidget_auxFilesCapture.on_addButton_clicked(0, [item.fileName,item.separator,header])

        # update capture and content header field values in gui
        self.gridWidgetCreator_captureFields.updateGridFieldValueWidgets(self.iFDO)

        # update custom header field values in gui
        self.setCurrent_nonStandard_headerFields()
        for item in self.currentiFDO_nonStandard_headerFields_list:
            self.nonStandardHeaderFieldListWidget.on_addButton_clicked(0,item)

    def setCurrent_nonStandard_headerFields(self):
        self.currentiFDO_nonStandard_headerFields_dict = {key: self.loadedHeaderFields.getHeaderField(key) for key, value in self.iFDO.ifdo_tmp[miqtv.image_set_header_key].items() if not key in miqtc.get_ifdo_fields()}
        self.currentiFDO_nonStandard_headerFields_list = [[key, self.loadedHeaderFields.getHeaderField(key)] for key, value in self.iFDO.ifdo_tmp[miqtv.image_set_header_key].items() if not key in miqtc.get_ifdo_fields()]

    def on_change_fct(self,change=None):
        #with miqtwidgets.Capturing() as output:
        
        self.tabValidate(False)
        self.setCustomInfoLabel.value =  self.notSetYetWarning
        self.outputCustomSetButton.clear_output()
        self.setCustomMsgWidget.value = ""
        #debugOutputWidget.addText(str(output))
    
    def getWidget(self):
        return self.myWidget
    
    def getTitle(self):
        return "Capture & Content Fields"

    
    
    
    

##### TAB: Create Capture & Content Fields ################################
    
    
class Tab_createcaptureAndContentFields(TabBase):
    
    def __init__(self,tabsCommon:TabsCommon,iFDO):
        TabBase.__init__(self,tabsCommon)
        
        createNonCoreFieldsButton = widgets.Button(description = "Create Capture and Content iFDO Fields",layout=widgets.Layout(width='auto'))
        createNonCoreFieldsButtonWidget = widgets.HBox([createNonCoreFieldsButton])
        self.createNonCoreFieldsButtonOutput = widgets.Output()

        def on_createNonCoreFieldsButton_click(b):
            self.createNonCoreFieldsButtonOutput.clear_output()
            with self.createNonCoreFieldsButtonOutput:

                print("Create capture and content fields:\n")
                try:
                    #iFDO.updateiFDOHeaderFields(header_update)
                    #iFDO.createCaptureAndContentFields()
                    iFDO.update_fields()
                    print("\nAll provided fields successfully created.")
                    self.tabValidate(True)
                except Exception as ex:
                    print( ex.args )
                    self.tabValidate(False)
                    return

        createNonCoreFieldsButton.on_click(on_createNonCoreFieldsButton_click)
        
        self.myWidget = widgets.VBox([
                                      miqtwidgets.VerticalSpacer(30),
                                      createNonCoreFieldsButtonWidget,
                                      self.createNonCoreFieldsButtonOutput,
                                      miqtwidgets.VerticalSpacer(30),
                                      self.nextTabButton])
        
        
    def getWidget(self):
        return self.myWidget
    
    def getTitle(self):
        return "Create Capture & Content Fields"
    
    def on_change_fct(self):
        self.createNonCoreFieldsButtonOutput.clear_output()
        self.tabValidate(False)
    
    


    
##### TAB: Write iFDO File ################################
    
    
class Tab_writeiFDOfile(TabBase):
    
    def __init__(self,tabsCommon:TabsCommon,iFDO,loadedHeaderFields,show_unused_fields:bool):
        TabBase.__init__(self,tabsCommon)
        self.iFDO = iFDO
        self.loadedHeaderFields = loadedHeaderFields
        self.show_unused_fields = show_unused_fields
        writeiFDOButton = widgets.Button(description = "Write iFDO File",layout=widgets.Layout(width='auto'))
        writeiFDOButtonWidget= widgets.HBox([writeiFDOButton])
        self.iFDOtargetFileChooser = FileChooser(os.path.dirname(self.iFDO.getiFDOFileName(overwrite=True)),os.path.basename(self.iFDO.getiFDOFileName(overwrite=True)))
        self.iFDOtargetFileChooser.filter_pattern = '*.yaml'
        self.iFDOtargetFileChooser._select.on_click(self.on_fileSelected)
        self.iFDOtargetFileChooser._apply_selection()
        self.selectTargetFIleNameOutput = widgets.Output()
        self.writeiFDOButtonOutput = widgets.Output()

        writeiFDOButton.on_click(self.on_writeiFDOButton_click)
        
        self.myWidget = widgets.VBox([
                                      miqtwidgets.VerticalSpacer(30),
                                      widgets.HBox([widgets.Label("Ouptut File:  "), self.iFDOtargetFileChooser]),
                                      self.selectTargetFIleNameOutput,
                                      miqtwidgets.VerticalSpacer(30),
                                      writeiFDOButtonWidget,
                                      miqtwidgets.VerticalSpacer(0),
                                      self.writeiFDOButtonOutput,
                                      miqtwidgets.VerticalSpacer(30),
                                      ])

    def on_fileSelected(self,b):
        if not self.iFDOtargetFileChooser.selected is None:
            self.writeiFDOButtonOutput.clear_output()
            self.selectTargetFIleNameOutput.clear_output()
            with self.selectTargetFIleNameOutput:
                self.iFDO.setiFDOFileName( self.iFDOtargetFileChooser.selected)
    
    def on_writeiFDOButton_click(self,b):
            self.writeiFDOButtonOutput.clear_output()
            with self.writeiFDOButtonOutput:
                try:
                    self.iFDO.write_ifdo_file()
                    print("Congratulations! An iFDO file was successfully created!")
                    
                    if len(self.loadedHeaderFields.unusedLoadedHeaderFields) != 0 and self.show_unused_fields:
                        print("\nFollowing fields have be been loaded but not been regarded in the wizzard (for debuggin only):")
                        print(self.loadedHeaderFields.unusedLoadedHeaderFields)
                except Exception as ex:
                    print( ex.args )
        
        
    def getWidget(self):
        return self.myWidget
    
    def getTitle(self):
        return "Write iFDO file"
    
    def on_change_fct(self):
        self.writeiFDOButtonOutput.clear_output()
        self.tabValidate(False)



class TestTab(TabBase):
    
    def __init__(self,tabsCommon:TabsCommon):
        TabBase.__init__(self,tabsCommon)
        
        checkButton = widgets.Button(description = "Check")
        checkButton.on_click(self.on_checkButton_clicked)
        self.myWidget = widgets.VBox([checkButton,miqtwidgets.VerticalSpacer(10),self.nextTabButton])
        #self.myWidget = widgets.VBox([checkButton,self.nextTabButton])
                
    def on_checkButton_clicked(self,b):
        self.tabValidate(True)
        
    def getWidget(self):
        return self.myWidget
    
    def getTitle(self):
        return "Test Tab"
    
    def on_change_fct(self):
        pass