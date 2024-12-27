from dtos.LabDTOs import LabGetDTO
from repositories.LabRepository import LabRepository


class LabService:
    @staticmethod
    async def get_all_labs() -> list[LabGetDTO]:
        lab_models = await LabRepository.get_all_labs()
        lab_get_dtos = [LabGetDTO(id=lab.id, name=lab.name, number=lab.number) for lab in lab_models]
        return lab_get_dtos