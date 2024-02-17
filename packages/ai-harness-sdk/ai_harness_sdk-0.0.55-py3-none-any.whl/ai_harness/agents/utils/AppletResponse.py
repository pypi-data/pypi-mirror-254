class SyncResponse:
    def __init__(self, answer : str, conversation_id : str, sources: list = None, thread_id: str = None):
        self.answer = answer
        self.conversation_id = conversation_id
        self.sources = sources
        self.thread_id = thread_id

    def obj(self):
        data = {"answer": self.answer, "conversation_id": self.conversation_id, "sources": self.sources, "thread_id" : self.thread_id}
        return data


class AsyncResponse:
    def __init__(self, answer):
        self.answer = answer

    def obj(self):
        data = {"answer": self.answer}
        return data
