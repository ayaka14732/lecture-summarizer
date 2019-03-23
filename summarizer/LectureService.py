from summarizer.tables import Lecture, Engine
from typing import List, Set, Dict


class LectureService(object):

    def __init__(self, memory_only=False):
        self.memory_only: bool = memory_only

    def create_lecture(self, request_body: Dict[str, str]) -> Dict[str, str]:
        session = Engine.get_instance(self.memory_only).Session()
        lecture = Lecture(
            name=request_body['name'],
            course=request_body['course'],
            content=request_body['content']
        )
        session.add(lecture)
        session.flush()
        session.commit()
        return {"id": lecture.id}

    def get_lecture(self, l_id) -> Dict[str, str]:
        session = Engine.get_instance(self.memory_only).Session()
        query = session.query(Lecture).filter(Lecture.id == l_id)
        lecture: Lecture = query.first()
        if lecture:
            return {
                'id': lecture.id,
                'name': lecture.name,
                'course': lecture.course,
                'content': lecture.content
            }
        return {}

    def get_lectures(self, query_params):
        return None
