from ninja import Router
from typing import List, Optional
from django.shortcuts import get_object_or_404
from prototyping.models.project_models import Project
from prototyping.models.user_models import User
from prototyping.schemas.project_schema import ProjectIn, ProjectOut
from prototyping.auth import QueryTokenAuth, HeaderTokenAuth
from datetime import datetime

project_router = Router(tags=["Projects"])

@project_router.post("/", response={201: ProjectOut}, auth=[QueryTokenAuth(), HeaderTokenAuth()])
def create_project(request, payload: ProjectIn):
    project_data = payload.dict(exclude={'users_ids', 'creation_date', 'last_release_date'})
    project_data['creation_date'] = datetime.strptime(payload.creation_date, "%Y-%m-%d").date() if payload.creation_date else None
    project_data['last_release_date'] = datetime.strptime(payload.last_release_date, "%Y-%m-%d").date() if payload.last_release_date else None
    
    project = Project.objects.create(**project_data)
    
    if payload.users_ids:
        users = User.objects.filter(id__in=payload.users_ids)
        project.users.set(users)
    
    project.save()
    return project

@project_router.get("/", response=List[ProjectOut], auth=[QueryTokenAuth(), HeaderTokenAuth()])
def read_projects(request, name: Optional[str] = None):
    if name:
        projects = Project.objects.filter(name__icontains=name)
    else:
        projects = Project.objects.all()
    return projects

@project_router.put("/{project_id}", response=ProjectOut, auth=[QueryTokenAuth(), HeaderTokenAuth()])
def update_project(request, project_id: int, payload: ProjectIn):
    project = get_object_or_404(Project, id=project_id)
    
    for attr, value in payload.dict(exclude={'users_ids', 'creation_date', 'last_release_date'}).items():
        setattr(project, attr, value)
    
    if payload.creation_date:
        project.creation_date = datetime.strptime(payload.creation_date, "%Y-%m-%d").date()
    if payload.last_release_date:
        project.last_release_date = datetime.strptime(payload.last_release_date, "%Y-%m-%d").date()
    
    if payload.users_ids is not None:
        users = User.objects.filter(id__in=payload.users_ids)
        project.users.set(users)
    
    project.save()
    return project

@project_router.delete("/{project_id}", response={204: None}, auth=[QueryTokenAuth(), HeaderTokenAuth()])
def delete_project(request, project_id: int):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return None
