# api/project_api.py
from ninja import Router
from typing import List, Optional
from django.shortcuts import get_object_or_404
from prototyping.models.project_models import Project
from prototyping.schemas.project_schema import ProjectIn, ProjectOut

project_router = Router(tags=["Projects"])

@project_router.post("/", response={201: ProjectOut})
def create_project(request, payload: ProjectIn):
    project = Project.objects.create(**payload.dict())
    return project

@project_router.get("/", response=List[ProjectOut])
def read_projects(request, name: Optional[str] = None):
    if name:
        projects = Project.objects.filter(name__icontains=name)
    else:
        projects = Project.objects.all()
    return projects

@project_router.put("/{project_id}", response=ProjectOut)
def update_project(request, project_id: int, payload: ProjectIn):
    project = get_object_or_404(Project, id=project_id)
    for attr, value in payload.dict().items():
        setattr(project, attr, value)
    project.save()
    return project

@project_router.delete("/{project_id}", response={204: None})
def delete_project(request, project_id: int):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return None
