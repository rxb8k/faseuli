from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import sys
sys.path.append("..")
from Money.models import *

# Create your views here.

def plan_main(request):
    user=request.user
    user_hobby=user.hobby 
    #user의 hobby를 가져옴
    plans=Plan.objects.filter(user=user)
    total_cost=0
    for p in plans:
        total_cost=total_cost+p.goal
    #recommend=로 해서 유저의 hobby에 따른 추천목록을 보여줘야함.
    recommend=RecommendPlan.objects.filter(hobby=user_hobby)
    Money_objects=Money.objects.filter(user=user)
    goal_cost=0
    for m in Money_objects:
        goal_cost=goal_cost+m.cost
    p=(goal_cost/total_cost)*100
    percent=round(p,2)
    if p>=100:
        percent=100
    return render(request,'plan_main.html',{'goal_cost':goal_cost,'plans':plans,'recommend':recommend,'user_hobby':user_hobby, 'total_cost':total_cost,'p':p,'percent':percent})

#플랜 작성하는 페이지로 이동하는 함수
def plan_add(request): 
    return render(request, 'plan_add.html')

def plan_create(request): 
    new_plan=Plan()
    new_plan.user=request.user
    new_plan.title=request.POST['title']
    new_plan.goal=request.POST['goal']
    new_plan.image=request.FILES.get('image')
    new_plan.save()
    #메인페이지로 이동??
    return redirect('plan:main')

def plan_del(request,id):
    delete=Plan.objects.get(id=id)
    delete.delete()
    return redirect('plan:main')

def edit_plan(request, id):
    edit=Plan.objects.get(id=id)
    #edit_plan.html로 이동
    return render(request, 'plan_edit.html',{'plan':edit})

def update_plan(request,id):
    update_plan=Plan.objects.get(id=id)
    update_plan.user=request.user
    update_plan.title=request.POST['title']
    update_plan.goal=request.POST['goal']
    update_plan.image=request.FILES.get('image')
    update_plan.save()
    return redirect('plan:main')
    