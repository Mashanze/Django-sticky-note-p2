from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteViewTest(TestCase):
    def setUp(self):
        # Create a sample note without the 'user' field
        self.note = Note.objects.create(
            title='Test Title', 
            content='Test Content'
        )

    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)

    def test_note_detail_view(self):
        response = self.client.get(reverse('note_detail', args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)