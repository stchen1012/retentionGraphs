from django.shortcuts import render
from django.http import HttpResponse

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import io
import psycopg2
import pandas as pd
from polls.models import Mytable
from django.template import loader
import base64
#imports for plotly here
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter


# Create your views here.


#keep below - this works
'''
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    #keeping the below lines of code for reference in case needed to reproduce error message
    #response = HttpResponse(content_type = 'image/png')
    #canvas = FigureCanvasAgg(fig)
    #canvas.print_png(response)

    FigureCanvasAgg(fig)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    return response

'''

#Below is the original code that didn't run
'''
def plot(request):
    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    response = HttpResponse(content_type = 'image/png')
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(response)
    return response
'''
'''
def index(request):
    #latest_list = Mytable.objects.order_by('id')[:5] #pulls last 5

    data = Mytable.objects.order_by('id')
    list_of_monthlyIncome = []
    list_of_jobSatisfication = []

    for i in data:
        list_of_monthlyIncome.append(i.monthlyincome)
        list_of_jobSatisfication.append(i.jobsatisfaction)

    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_list': latest_list, 
    # }
    # return HttpResponse(template.render(context, request))
    print(list_of_monthlyIncome)
    print(list_of_jobSatisfication)
    return HttpResponse(list_of_jobSatisfication)
'''
'''
def index(request):
    # Data for plotting
    data = Mytable.objects.order_by('id')
    list_of_monthlyincome = []
    list_of_jobsatisfication = []
    list_of_age = []
    list_of_attrition = []
    list_of_businesstravel = []
    list_of_distancefromhome = []
    list_of_gender = []
    list_of_maritalstatus = []
    list_of_numcompaniesworked = []
    list_of_stockoptionlevel = []
    list_of_relationshipsatisfaction = []
    list_of_trainingtimeslastyear = []
    list_of_worklifebalance = []
    list_of_yearsatcompany = []
    list_of_yearssincelastpromotion = []
    list_of_yearswithcurrmanager = []
    singleGone = 0
    marriedGone = 0
    divorcedGone = 0
    jobSatOneGone = 0
    jobSatTwoGone = 0
    jobSatThreeGone = 0
    jobSatFourGone = 0
    maleGone = 0
    femaleGone = 0

    for i in data:
        if(i.attrition == 'Yes' and i.maritalstatus == 'Single'):
            singleGone += 1
        if(i.attrition == 'Yes' and i.maritalstatus == 'Divorced'):
            marriedGone += 1
        if(i.attrition == 'Yes' and i.maritalstatus == 'Married'):
            divorcedGone += 1
        if(i.attrition == 'Yes' and i.jobsatisfaction == 1):
            jobSatOneGone += 1
        if(i.attrition == 'Yes' and i.jobsatisfaction == 2):
            jobSatTwoGone += 1
        if(i.attrition == 'Yes' and i.jobsatisfaction == 3):
            jobSatThreeGone += 1
        if(i.attrition == 'Yes' and i.jobsatisfaction == 4):
            jobSatFourGone += 1
        if(i.attrition == 'Yes' and i.gender == 'Male'):
            maleGone += 1
        if(i.attrition == 'Yes' and i.gender == 'Female'):
            femaleGone += 1

        list_of_age.append(i.age)
        list_of_monthlyincome.append(i.monthlyincome)
        list_of_jobsatisfication.append(i.jobsatisfaction)
        list_of_attrition.append(i.attrition)
        list_of_businesstravel.append(i.businesstravel)
        list_of_distancefromhome.append(i.distancefromhome)
        list_of_gender.append(i.gender)
        list_of_maritalstatus.append(i.maritalstatus)
        list_of_numcompaniesworked.append(i.numcompaniesworked)
        list_of_stockoptionlevel.append(i.stockoptionlevel)
        list_of_relationshipsatisfaction.append(i.relationshipsatisfaction)
        list_of_trainingtimeslastyear.append(i.trainingtimeslastyear)
        list_of_worklifebalance.append(i.worklifebalance)
        list_of_yearsatcompany.append(i.yearsatcompany)
        list_of_yearssincelastpromotion.append(i.yearssincelastpromotion)
        list_of_yearswithcurrmanager.append(i.yearswithcurrmanager)
    # t = np.arange(0.0, 2.0, 0.01)
    # s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(list_of_monthlyincome, list_of_jobsatisfication, 'o')

    ax.set(xlabel= 'Monthly Income ($)', ylabel='Job Satisification',
           title='Job Satisification and Monthly Income - all data')
    ax.grid()

    FigureCanvasAgg(fig)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    #return response
    
    img_str = base64.b64encode(buf.getvalue())
    data_url = 'data:image/jpg;base64,' + base64.b64encode(buf.getvalue()).decode()
    # I recommend to add Content-Length for Django
    #response['Content-Length'] = str(len(response.content))
    #
    #return response

    # graph
    fig, ax = plt.subplots()
    ax.plot(list_of_age, list_of_yearsatcompany, 'o')
    #ax.plot(list_of_age, list_of_jobsatisfication)

    ax.set(xlabel= 'Age', ylabel='# of years',
           title='Age and Num of Years at Company - all data')
    ax.grid()

    ax2 = ax.twinx() #instantiate a second axes that shares that same x-axis

    color = 'tab:red'
    ax2.set_ylabel('Satisfication', color = color)
    ax2.plot(list_of_age, list_of_jobsatisfication, 'o', color = color)
    ax2.tick_params(axis='y', labelcolor=color)

    FigureCanvasAgg(fig)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    img_str = base64.b64encode(buf.getvalue())
    data_age_url = 'data:image/jpg;base64,' + base64.b64encode(buf.getvalue()).decode()

    
    #gender single bar graph - this works below - keep
    # fig, ax = plt.subplots()
    # male = list_of_gender.count('Male')
    # female = list_of_gender.count('Female')
    # plt.bar(['Male', 'Female'], [male, female], color = "orange")
    # plt.xlabel('Gender')
    # plt.ylabel('Count')
    # plt.title('Gender breakdown')
    # plt.show()

    # FigureCanvasAgg(fig)
    # buf = io.BytesIO()
    # plt.savefig(buf, format='png')
    # plt.close(fig)
    # response = HttpResponse(buf.getvalue(), content_type='image/png')
    # img_str = base64.b64encode(buf.getvalue())
    # data_gender_url = 'data:image/jpg;base64,' + base64.b64encode(buf.getvalue()).decode()

    #gender bar graph analysis with attrition
    fig, ax = plt.subplots()
    male = list_of_gender.count('Male')
    female = list_of_gender.count('Female')
    plt.bar(['Male', 'Female'], [male, female], color = "orange")
    plt.bar(['Male', 'Female'], [maleGone, femaleGone], color = "yellow")
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.title('Gender Breakdown and Attrition')
    plt.legend(['Current', 'Churned'])
    rectangles = ax.patches
    malePercentage = str(round((maleGone/male) * 100)) + '%'
    femalePercentage = str(round((femaleGone/female) * 100)) + '%'
    barLabels = [malePercentage, femalePercentage]

    # Make some labels.
    #labels = ["label%d" % i for i in range(len(rects)-4)]

    for rect, label in zip(rectangles, barLabels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')
    plt.show()

    FigureCanvasAgg(fig)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    img_str = base64.b64encode(buf.getvalue())
    data_gender_url = 'data:image/jpg;base64,' + base64.b64encode(buf.getvalue()).decode()



    #number of employees single bar graph
    #why doesn't width attribute work here?

    fig, ax = plt.subplots()
    plt.bar('Employee - 1470', [len(list_of_gender)], color = "red", width = .1)
    
    plt.xlabel('Employees')
    plt.ylabel('Count')
    plt.title('Total # of Employees (including churned)')
    plt.show()

    FigureCanvasAgg(fig)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    
    img_str = base64.b64encode(buf.getvalue())
    data_employeecount_url = 'data:image/jpg;base64,' + base64.b64encode(buf.getvalue()).decode()

    #marriage double bar (it is stacked because width parameter isn't added) graph
    fig, ax = plt.subplots()
    divorced = list_of_maritalstatus.count('Divorced')
    married = list_of_maritalstatus.count('Married')
    single = list_of_maritalstatus.count('Single')
     
    plt.bar(['Single', 'Married', 'Divorced'], [single, married, divorced], color = "purple")
    plt.bar(['Single', 'Married', 'Divorced'], [singleGone, marriedGone, divorcedGone], color = "yellow")
    plt.xlabel('Marital Status')
    plt.ylabel('Count')
    plt.title('Marital Status and Attrition')
    plt.legend(["Current", "Churned"])

    rectangles = ax.patches
    divorcedPercentage = str(round((divorcedGone/divorced) * 100)) + '%'
    marriedPercentage = str(round((marriedGone/married) * 100)) + '%'
    singlePercentage = str(round((singleGone/single) * 100)) + '%'
    arrLabels = [singlePercentage, marriedPercentage, divorcedPercentage]

    # Make some labels.
    #labels = ["label%d" % i for i in range(len(rects)-4)]

    for rect, label in zip(rectangles, arrLabels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')
    plt.show()

    FigureCanvasAgg(fig)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    img_str = base64.b64encode(buf.getvalue())
    data_maritalattrition_url = 'data:image/jpg;base64,' + base64.b64encode(buf.getvalue()).decode()

    #job satisification and attrition double bar with width parameter
    fig, ax = plt.subplots()
    width = 0.3
    countJobSatOne = list_of_jobsatisfication.count(1)
    countJobSatTwo = list_of_jobsatisfication.count(2)
    countJobSatThree = list_of_jobsatisfication.count(3)
    countJobSatFour = list_of_jobsatisfication.count(4)

    plt.bar(['1', '2', '3', '4'], [countJobSatOne, countJobSatTwo, countJobSatThree, countJobSatFour], width = width, color = "blue")
    plt.bar(['1', '2', '3', '4'], [jobSatOneGone, jobSatTwoGone, jobSatThreeGone, jobSatFourGone], width = width, color = "yellow")
    plt.xlabel('Job Satisfaction')
    plt.ylabel('Count')
    plt.title('Job Satisification and Attrition')
    plt.legend(["Current", "Churned"])
    
    rects = ax.patches
    jobSatOnePercentage = str(round((jobSatOneGone/countJobSatOne) * 100)) + '%'
    jobSatTwoPercentage = str(round((jobSatTwoGone/countJobSatTwo) * 100)) + '%'
    jobSatThreePercentage = str(round((jobSatThreeGone/countJobSatThree) * 100)) + '%'
    jobSatFourPercentage = str(round((jobSatFourGone/countJobSatFour) * 100)) + '%'
    arrOfLabels = [jobSatOnePercentage, jobSatTwoPercentage, jobSatThreePercentage, jobSatFourPercentage]

    # Make some labels.
    #labels = ["label%d" % i for i in range(len(rects)-4)]

    for rect, label in zip(rects, arrOfLabels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label, ha='center', va='bottom')
    plt.show()

    FigureCanvasAgg(fig)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    img_str = base64.b64encode(buf.getvalue())
    data_barJobSat_url = 'data:image/jpg;base64,' + base64.b64encode(buf.getvalue()).decode()

    #distance from work 
    
    #figsize below alters dimension graph
    fig, ax = plt.subplots(figsize=(12,4))
    
    plt.bar(range(len(list_of_distancefromhome)), list_of_distancefromhome, color = "royalblue", alpha=0.7)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
    plt.xlabel('Employee')
    plt.ylabel('Distance from home')
    plt.title("Each employee's distance from home")
    plt.show()

    FigureCanvasAgg(fig)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    img_str = base64.b64encode(buf.getvalue())
    data_barDistance_url = 'data:image/jpg;base64,' + base64.b64encode(buf.getvalue()).decode()

    return render(request, "polls/index.html", {'image': data_url, 'image_age': data_age_url, 'image_gender': data_gender_url, 'image_employeecount': data_employeecount_url, 'image_marital_attrition': data_maritalattrition_url, 'image_barJobSat': data_barJobSat_url, 'image_barDistance': data_barDistance_url })
    '''

    #plotly

def index(request):
    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request, "polls/index.html", context={'plot_div': plot_div})
