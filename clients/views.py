from django.shortcuts import render
from clients.models import *
from forms import *
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from socket import *
import os, sys, fileinput, re, datetime
import unicodedata
# Create your views here.

def main_view(request):
        return render(request, 'clients/main.html')

        

def clients_search(request):
    Client_fw.objects.all().delete()
    directory = '/home/puchto/Dropbox/Nauka2015/pythonscripts/pliki_robocze/krowa_workfiles/'
    form = Search_add(request.POST or None)
    if form.is_valid():
        if form.cleaned_data['address_nrd']:
            search_str = form.cleaned_data['address_ul'] + '_' + form.cleaned_data['address_nrd']
        elif form.cleaned_data['address_nrm']:
            search_str = form.cleaned_data['address_ul'] + '_' + form.cleaned_data['address_nrd'] + '_' + form.cleaned_data['address_nrm']
        elif not form.cleaned_data['address_nrm']:
            search_str = form.cleaned_data['address_ul']
        #search_str = form.cleaned_data['address_ul'] + '_' + form.cleaned_data['address_nrd'] + '_' + form.cleaned_data['address_nrm']
        filelist = [f for f in os.listdir(directory) if os.path.isfile(directory + f)]
        for x in range(len(filelist)):
            tmp_file = filelist[x]
            filelist[x] = directory + filelist[x]
            with open(filelist[x]) as currentfile:
                text = currentfile.read()
                if search_str in text:
                    with open(filelist[x]) as f:
                        for i, line in enumerate(f,0):
                            if search_str in line:
                                rec = line.split('|')
                                if len(rec[0].split('_')) == 1:
                                    cl_add_ul = rec[0]
                                    cl_add_nrd = ''
                                    cl_add_nrm = ''
                                    cl_add_rect = ''
                                elif len(rec[0].split('_')) == 2:
                                    cl_add_ul = rec[0].split('_')[0]
                                    cl_add_nrd = rec[0].split('_')[1]
                                    cl_add_nrm = ''
                                    cl_add_rect = ''
                                elif len(rec[0].split('_')) == 3:
                                    cl_add_ul = rec[0].split('_')[0]
                                    cl_add_nrd = rec[0].split('_')[1]
                                    cl_add_nrm = rec[0].split('_')[2]
                                    cl_add_rect = ''
                                elif len(rec[0].split('_')) == 4:
                                    cl_add_ul = rec[0].split('_')[0]
                                    cl_add_nrd = rec[0].split('_')[1]
                                    cl_add_nrm = rec[0].split('_')[2]
                                    cl_add_rect = rec[0].split('_')[3]
                                elif len(rec[0].split('_')) == 5:
                                    cl_add_ul = rec[0].split('_')[0]
                                    cl_add_nrd = rec[0].split('_')[1]
                                    cl_add_nrm = rec[0].split('_')[2]
                                    cl_add_rect = rec[0].split('_')[3] + rec[0].split('_')[4]
                                    
                                    
                                    
                                cl = Client_fw(
                                               loc_file = tmp_file,
                                               ln_nr = i,
                                               cl_address_ul = cl_add_ul,
                                               cl_address_nr_d = cl_add_nrd,
                                               cl_address_nr_m = cl_add_nrm,
                                               cl_address_rest = cl_add_rect,
                                               mac = rec[1],
                                               ip_add = rec[2],
                                               kl_service = rec[3],
                                               downl = rec[4],
                                               upl = rec[5]
                                               )
                                cl.save()
                        
                
        clients = Client_fw.objects.all().order_by('cl_address_ul')   
        return render(request, 'clients/clients_found.html', {'clients': clients})
    return render(request, 'clients/clients_search.html', {'form': form})


def clients_found(request):
    clients_active = Client_fw.objects.all().order_by('cl_address_ul')
    return render(request, 'clients/clients_found.html', {'clients': clients_active})


def client_edit_Client_fw(request, pk):
        client = get_object_or_404(Client_fw, pk=pk)
        form = Edit_form_CClient_fw(request.POST or None, instance = client)
        if form.is_valid():
                form.save()
                return redirect('client_info_fw', pk=pk)
        return render(request, 'clients/clients_edit_Clients_fw.html', {'client': client, 'form': form})

def client_info_fw(request, pk):
    client = get_object_or_404(Client_fw, pk=pk)
    return render(request, 'clients/client_info_fw.html', {'client': client})



def clients_list(request):
        ###clients_active = Auth_record.objects.filter(kl_service = 0).order_by('cl_address')
        clients_active = Auth_record.objects.all().order_by('cl_address')
        return render(request, 'clients/clients_list.html', {'clients': clients_active})


def client_info(request, pk):
        client = get_object_or_404(Auth_record, pk=pk)
        return render(request, 'clients/client_info.html', {'client': client})


def client_edit(request, pk):
        client = get_object_or_404(Auth_record, pk=pk)
        form = Edit_form(request.POST or None, instance = client)
        if form.is_valid():
                form.save()
                return redirect('client_info', pk=pk)
        return render(request, 'clients/client_edit.html', {'client': client, 'form': form})
        

    
def clients_arp(request):
    Arp_ent.objects.all().delete()
    
    with open('/home/puchto/djangoprojects/LAN1/arp_act_only.txt') as currf:
        for i, line in enumerate(currf, 0):
                rec = line.split()
                arprec = Arp_ent(cl_address=rec[0], mac=rec[2])
                arprec.save()
    clients = Arp_ent.objects.all().order_by('cl_address')
    return render(request, 'clients/clients_arp.html', {'clients': clients})

def show_clients(request):
        clients = Client_rec.objects.all().order_by('cl_address')
        return render(request, 'clients/clients_list.html', {'clients': clients})
    
'''
#funckja szukajaca klientow w zaimportowanej DB
def clients_search(request):
        form = Src_form(request.POST or None)
        if form.is_valid():
                clients = Auth_record.objects.filter(cl_address__contains = form.cleaned_data['address']).order_by('cl_address')
                return render(request, 'clients/clients_list.html', {'clients': clients})
        return render(request, 'clients/clients_search.html', {'form': form})
'''


'''
#funkcja operujacy na netmaster i kiel z laptopa z vpn
def clients_arp(request):
        Arp_ent.objects.all().delete()
        res = send_to_kiel('arp')
        res1 = str(res).split(';')
        for rec in res1:
                arprec = Arp_ent(cl_address=rec.split('|')[0], mac=rec.split('|')[1])
                arprec.save()
        
        clients = Arp_ent.objects.all().order_by('cl_address')
        return render(request, 'clients/clients_arp.html', {'clients': clients})
'''    

'''
#funkcja operujaca na netmaster i kiel z laptopa z vpn
def clients_search(request):
        Client_rec.objects.all().delete()
        form = Src_form(request.POST or None)
        if form.is_valid():
                res = send_to_kiel('1%' + form.cleaned_data['address'])
                res1 = str(res).split(';')
                for rec in res1:
                        cl = Client_rec(
                                loc_file=rec.split('|')[0],
                                ln_nr = rec.split('|')[1],
                                cl_address=rec.split('|')[2],
                                mac=rec.split('|')[3],
                                ip_add=rec.split('|')[4],
                                kl_service=rec.split('|')[5],
                                downl=rec.split('|')[6],
                                upl=rec.split('|')[7]
                                )
                        cl.save()
                clients = Client_rec.objects.all().order_by('cl_address')
                return render(request, 'clients/clients_list.html', {'clients': clients})
                
        return render(request, 'clients/clients_search.html', {'form': form})

#funkcja operujaca na netmaster i kiel z laptopa z vpn
def client_edit(request, pk):
        client = get_object_or_404(Client_rec, pk=pk)
        form = Edit_form(request.POST or None, instance = client)
        if form.is_valid():
                form.save()
                
                send_str = '2%' + str(client.loc_file) + ';' + str(client.ln_nr) + ';'
                send_str2 = [
                            client.cl_address,
                            client.mac,
                            client.ip_add,
                            client.kl_service,
                            client.downl,
                            client.upl
                            ]

                res = (send_str.strip() + ('|').join(send_str2))
                result = send_to_kiel(res)
                
                return render(request, 'clients/main.html')
                
        return render(request, 'clients/client_edit.html', {'client': client, 'form': form})
                        
'''

                

def send_to_kiel(lista):
    serverHost = '192.168.11.4'            
    serverPort = 2163               
    s = socket(AF_INET, SOCK_STREAM)    
    s.connect((serverHost, serverPort))
    s.send(unicodedata.normalize('NFKD', lista).encode('ascii', 'ignore'))               
    data = s.recv(20480)                 
    return data