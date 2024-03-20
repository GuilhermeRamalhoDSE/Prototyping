from ninja import Router
from typing import List, Optional
from django.shortcuts import get_object_or_404
from prototyping.models.project_models import Project
from prototyping.models.user_models import User
from prototyping.schemas.project_schema import ProjectIn, ProjectOut, UserIdSchema, UserOut
from prototyping.auth import QueryTokenAuth, HeaderTokenAuth
from datetime import datetime
from prototyping.utils import check_user_permission, get_user_info_from_token

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

@project_router.post("/{project_id}/add-user/", response={200: ProjectOut}, auth=[QueryTokenAuth(), HeaderTokenAuth()])
def add_user_to_project(request, project_id: int, payload: UserIdSchema):
    if not check_user_permission(request):
        return {"detail": "Permission denied."}, 403

    project = get_object_or_404(Project, id=project_id)
    user = get_object_or_404(User, id=payload.user_id)
    
    if not project.users.filter(id=user.id).exists():
        project.users.add(user)
        project.save()

    return generate_project_response(project)

@project_router.post("/{project_id}/remove-user/", response={200: ProjectOut}, auth=[QueryTokenAuth(), HeaderTokenAuth()])
def remove_user_from_project(request, project_id: int, payload: UserIdSchema):
    if not check_user_permission(request):
        return {"detail": "Permission denied."}, 403

    project = get_object_or_404(Project, id=project_id)
    user = get_object_or_404(User, id=payload.user_id)
    
    if project.users.filter(id=user.id).exists():
        project.users.remove(user)
        project.save()

    return generate_project_response(project)

@project_router.get("/", response=List[ProjectOut], auth=[QueryTokenAuth(), HeaderTokenAuth()])
def read_projects(request):
    user_info = get_user_info_from_token(request)
    user_id = user_info.get('user_id') 
    is_superuser = user_info.get('is_superuser', False) in [True, 'True', 'true', 1, '1']
    is_staff = user_info.get('is_staff', False) in [True, 'True', 'true', 1, '1'] 
  

    if is_superuser:
        projects_query = Project.objects.all()
    elif is_staff:
        license_id = user_info.get('license_id')
        projects_query = Project.objects.filter(client__license_id=license_id)
    else:
        projects_query = Project.objects.filter(users__id=user_id)

    projects = list(projects_query)

    projects_response = [generate_project_response(project) for project in projects]
    
    return projects_response


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

def generate_project_response(project):
    users_data = [UserOut(id=user.id, full_name=f"{user.first_name} {user.last_name}") for user in project.users.all()]

    project_data = {
        "id": project.id,
        "client_id": project.client.id,
        "name": project.name,
        "start_date": project.start_date,
        "end_date": project.end_date,
        "users": users_data,
    }
    return ProjectOut(**project_data)
