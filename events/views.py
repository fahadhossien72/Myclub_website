from audioop import lin2adpcm
from urllib import request, response
from . models import *
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import FileResponse, HttpResponse
import calendar 
from calendar import HTMLCalendar
from datetime import datetime
from . forms import *
import csv

import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from . utilis import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = 'Fahadhossien'
    #convert month name to number
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    #create a calender
    cal = HTMLCalendar().formatmonth(year, month_number)
    #Get current Year
    now = datetime.now()
    current_year = now.year
    #Get Current time
    time = now.strftime('%I:%M:%p')
    context = {'name':name, 'year':year, 'month':month,
     'month_number':month_number, 'cal':cal, 'current_year':current_year, 'time':time}
    return render(request, 'events/home.html', context)

@login_required(login_url='login')
def all_event(request):
    event_list = Event.objects.all().order_by('name')
    context = {'events':event_list}
    return render(request, 'events/event_list.html', context)

@login_required(login_url='login')
def createEvent(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event')
    context = {'form':form}
    return render(request, 'events/create-event.html', context)

@login_required(login_url='login')
def update_event(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event')
    context = {'event': event, 'form':form}
    return render(request, 'events/create-event.html', context)

@login_required(login_url='login')
def delete_event(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == "POST":
        event.delete()
        return redirect('event')
    context = {'event':event}
    return render(request, 'events/delete-event.html', context)


@login_required(login_url='login')
def createVenue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create-venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    context = {'form':form, 'submitted':submitted}
    return render(request, 'events/create-venue.html', context)

@login_required(login_url='login')
def list_venue(request):
    venues = Venue.objects.all()
    venues, paginator, custom_range = paginatorVenue(request, venues, 2)
    context = {'venues': venues, 'paginator':paginator, 'custom_range':custom_range}
    return render(request, 'events/venue-list.html', context)

@login_required(login_url='login')
def update_venue(request, pk):
    venue = Venue.objects.get(id=pk)
    form = VenueForm(instance=venue)
    if request.method == "POST":
        form = VenueForm(request.POST, instance=venue)
        if form.is_valid():
            form.save()
            return redirect('venue-list')
    context = {'venues': venue, 'form':form}
  
    return render(request, 'events/create-venue.html', context)

@login_required(login_url='login')
def delete_venue(request, pk):
    venue = Venue.objects.get(id=pk)
    if request.method == "POST":
        venue.delete()
        return redirect('venue-list')
    context = {'venue':venue}
    return render(request, 'events/delete-venue.html', context)

@login_required(login_url='login')
def show_venue(request, pk):
    venue = Venue.objects.get(id=pk)
    context = {'venue':venue}
    return render(request, 'events/venue-show.html', context)

@login_required(login_url='login')
def search_venue(request):
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
    venue = Venue.objects.filter(name__icontains=search)

    context = {'search':search, 'venues':venue}
    return render(request, 'events/search-venue.html', context)

@login_required(login_url='login')
#Generate Text file in Venue_list
def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.txt'

    venues = Venue.objects.all()

    lines = []

    for venue in venues:
        lines.append(f'{venue.name}\n {venue.address}\n {venue.zip_code}\n{venue.web}\n{venue.phone}\n{venue.email_address}\n\n\n')
    

    response.writelines(lines)
    return response

@login_required(login_url='login')
#Generate CSV file in Venue_list
def venue_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venues.csv'
    #create csv writter
    writer = csv.writer(response)
    venues = Venue.objects.all()
    # Add coloum for csv file
    writer.writerow(['Venue Name', 'Address', 'Zip Code', 'Web', 'Phone', 'Email' ])

    for venue in venues:
        writer.writerow([venue.name, venue.address, venue.zip_code, venue.web, venue.phone, venue.email_address])
    
    return response

@login_required(login_url='login')
#Generate Pdf file in Venue_list
def venue_pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=letter, bottomup=0)

    #create a text object
    textob = p.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    venues = Venue.objects.all()
    # Add some line 
    lines = []
 
    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.zip_code)
        lines.append(venue.web)
        lines.append(venue.phone)
        lines.append(venue.email_address)
        lines.append("=========================")
    #loop
    for line in lines:
        textob.textLine(line)
    
    #finish up
    p.drawText(textob)
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='venue.pdf')


