from dtos.LabDTOs import LabGetDTO, LabAddDTO
from models.LabsModel import LectureTimes, LabsModel
from repositories.LabRepository import LabRepository
from services.DatetimeService import DatetimeService


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

    @staticmethod
    async def update_lab_last_update_time(lab_id: int, new_last_updated_date: str):
        new_last_update_date_datetime = DatetimeService.convert_date_string_to_datetime(new_last_updated_date)
        await LabRepository.update_lab_last_update_time(lab_id, new_last_update_date_datetime)

    @staticmethod
    async def create_lab(new_lab: LabAddDTO):
        new_lab_model = LabsModel(name=new_lab.name, number=new_lab.number)
        await LabRepository.create_lab(new_lab_model)