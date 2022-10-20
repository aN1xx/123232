from rest_framework.views import APIView
from .models import Sample, Chapter
from io import BytesIO
from docx import Document
from django.http import StreamingHttpResponse



class ExportDocx(APIView):
    def get(self, request, *args, **kwargs):
        document = self.build_document()
        buffer = BytesIO()
        document.save(buffer)
        buffer.seek(0)
        response = StreamingHttpResponse(
            streaming_content=buffer,
            content_type='application/vnd.openxmlformats-'
                         'officedocument.wordprocessingml.document'
        )
        response['Content-Disposition'] = 'attachment;filename=Test.docx'
        response["Content-Encoding"] = 'UTF-8'
        return response

    def build_document(self):
        pass