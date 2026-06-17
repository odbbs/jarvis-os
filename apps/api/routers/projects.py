from fastapi import APIRouter

from packages.projects.registry import ProjectRegistry

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.get("")
async def list_projects():
    registry = ProjectRegistry()
    return {"projects": registry.list_all()}


@router.get("/{project_id}")
async def get_project(project_id: str):
    registry = ProjectRegistry()
    project = registry.get(project_id)
    if not project:
        return {"error": f"Project '{project_id}' not found"}, 404
    return {"project": project}
