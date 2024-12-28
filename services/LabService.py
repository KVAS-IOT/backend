from dtos.LabDTOs import LabGetDTO
from models.LabsModel import LectureTimes
from repositories.LabRepository import LabRepository


class LabService:
    @staticmethod
    async def get_all_labs() -> list[LabGetDTO]:
        lab_models = await LabRepository.get_all_labs()
        lab_get_dtos = [LabGetDTO(id=lab.id, name=lab.name, number=lab.number, last_updated_date=lab.last_updated_date) for lab in lab_models]
        return lab_get_dtos

    @staticmethod
    async def get_lab_lecture_times_by_lab_id(lab_id: int) -> list[LectureTimes]:
        lab_lecture_times = await LabRepository.get_lab_lecture_times_by_lab_id(lab_id)
        return lab_lecture_times