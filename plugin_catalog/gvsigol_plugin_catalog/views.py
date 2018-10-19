# -*- coding: utf-8 -*-

'''
    gvSIG Online.
    Copyright (C) 2010-2017 SCOLAB.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

'''
@author: jrodrigo <jrodrigo@scolab.es>
'''


from django.shortcuts import render_to_response, RequestContext, redirect, HttpResponse
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotFound, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_safe,require_POST, require_GET
from django.shortcuts import render
import json
import ast
from django.views.decorators.csrf import csrf_exempt
from service import geonetwork_service


def get_query(request):
    
    if geonetwork_service!=None and request.method == 'GET':
        try:
            parameters = request.GET
            
            query = ''
            for key in parameters:
                query += key+'='
                for item in parameters.get(key):
                    query+=item
                query += '&'
            
            response = geonetwork_service.get_query(query)
            aux_response = json.loads(response)
            return HttpResponse(response, content_type='text/plain')
        except Exception as e:
            return HttpResponse(status=500, content=e.message)
        
    return HttpResponse(status=500)

def get_metadata(request, metadata_id):
    
    if geonetwork_service!=None and request.method == 'GET':
        try:
            parameters = request.GET
            get_panel = False
            if 'getPanel' in parameters:
                get_panel = True
                
            response = geonetwork_service.get_metadata(metadata_id)
            #aux_response = json.loads(response)
                     
            if not response:
                return  HttpResponse(json.dumps({}, indent=4), content_type='application/json')
            if get_panel:
                #http://localhost/gvsigonline/catalog/get_metadata/<metadata_id>/?getPanel=true
                html = '<div class="row" style="padding: 20px;">'
                html += '    <div class="col-md-8">'
                html += '        <h4 class="modal-catalog-title" style="font-weight:bold">'+response['title']+'</h4>'
                html += '        <p>'+response['abstract']+'</p>'
        
                html += '        <br /><br /><p class="catalog_content_title block-with-text">'+'About this resource'+'</p>'
                html += '        <span>'+'Categories'+':</span>'
                
                categories = ''
                cat_count = 0
                for cat in response['categories']:
                    if cat and cat.strip() != '':
                        if cat_count > 0:
                            categories += ',' + cat
                        else:
                            categories += cat
                            cat_count += 1
                
                html += '        '+ categories
                html += '        <br />'
       
                html += '        <span>'+'Keywords'+':</span>'
                keywords = ''
                key_count = 0
                for key in response['keywords']:
                    if key and key.strip() != '':
                        if key_count > 0:
                            keywords += ',' + key
                        else:
                            keywords += key
                            key_count += 1
                            
                html += '        '+ keywords
                html += '        <br />'
               
                html += '        <span>'+'Legal constraints'+':</span>'
                html += '        .......TO DO....'
                html += '        <br />'
            
                html += '        <br /><br /><p class="catalog_content_title block-with-text">'+'Technical information'+':</p>'
                   
                html += '        <span>'+'Representation type'+':</span>'
                html += '        '+response['representation_type']
                html += '        <br />'
                        
                html += '        <span>'+'Scale'+':</span>'
                html += '        1:'+response['scale']
                html += '        <br />'
                        
                html += '        <span>'+'Coordinate Reference System'+':</span>'
                html += '        '+response['srs']
                html += '        <br />'
                        
                html += '        <span>'+'Metadata identifier'+':</span>'
                html += '        '+response['metadata_id']
                html += '        <br />'
                        
                html += '    </div>'
                html += '    <div class="col-md-4">'
                for thumbnail in response['thumbnails']:
                    html += '            <img src="'+thumbnail['url']+'" alt="'+thumbnail['name']+'"/><br />'
                    
                html += '        <br /><br /><p class="catalog_content_title block-with-text">'+'Download and links'+':</p>'
                for resource in response['resources']:
                    default_key = 'name'
                    if not resource[default_key]:
                        default_key = 'descriptions'
                    html += '            '+ str(resource[default_key])
                    if resource['protocol'] == 'WWW:DOWNLOAD-1.0-http--download':
                        html += '                <a href="'+resource['url']+'" target="_blank" style="float:right; background-color:#eee; padding:5px; width:75px">Download</a>'
                    if resource['protocol'] == "OGC:WMS":
                        html += '                <a href="'+resource['url']+'?service=WMS&request=GetCapabilities" target="_blank" style="float:right; background-color:#eee; padding:5px; width:75px">OGC:WMS</a>'
                    if resource['protocol'] == "OGC:WFS-1.0.0-http-get-capabilities":
                        html += '                <a href="'+resource['url']+'?service=WFS&version=1.0.0&request=GetFeature&typeName='+str(resource['name'])+'&outputFormat=SHAPE-ZIP" target="_blank" style="float:right; background-color:#eee; padding:5px; width:75px">Get shape</a>'
                    html += '            <div style="clear:both"></div>'
                
                html += '        <br /><br /><p class="catalog_content_title block-with-text">'+'Spatial Extent'+':</p>'
                html += '        <img class="gn-img-thumbnail img-thumbnail gn-img-extent" data-ng-src="'+response['image_url']+'" src="'+response['image_url']+'"/>'
                        
                html += '        <br /><br /><p class="catalog_content_title block-with-text">'+'Temporal Extent'+':</p>'
                html += '        <span>'+'Publication date'+':</span>'
                html += '        '+response['publish_date']
                html += '        <br />'
                        
                html += '        <span>'+'Period'+':</span>'
                html += '        '+response['period_start']+' - '+response['period_end']
                html += '        <br />'
                        
                html += '    </div>'
                html += '</div>' 
                
                response['html']= html
                
                return  HttpResponse(json.dumps(response, indent=4), content_type='application/json')
            else:
                #http://localhost/gvsigonline/catalog/get_metadata/<metadata_id>/
                return render_to_response('catalog_details.html', response, context_instance=RequestContext(request))
            
        except Exception as e:
            return HttpResponse(status=500, content=e.message)
        
    return HttpResponse(status=500)


'''
@require_http_methods(["GET"])
def metadata_form(request, metadata_id):
    
    if geonetwork_service!=None and request.method == 'GET':
        response = geonetwork_service.metadata_editor(metadata_id)
        return HttpResponse(response, content_type='text/plain')
        
    return HttpResponse(status=500)
    
'''