from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteModelTest(TestCase):
    def setUp(self):
        # Create a sample note for model testing
        Note.objects.create(
            title='Test Note Title',
            content='This is test note content.',
            color='light cloud'
        )

    def test_note_has_title(self):
        # Test that the note title matches expected value
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note Title')

    def test_note_has_content(self):
        # Test that the note content matches expected value
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is test note content.')

    def test_note_default_color(self):
        # Test the color field value
        note = Note.objects.get(id=1)
        self.assertEqual(note.color, 'light cloud')


class NoteViewTest(TestCase):
    def setUp(self):
        # Create a sample note for view testing
        Note.objects.create(
            title='View Test Note',
            content='Testing the list and delete views.',
            color='mint green'
        )

    def test_note_list_view(self):
        # Test that the note list view loads successfully (status code 200) and contains note text
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'View Test Note')

    def test_note_creation_view(self):
        # Test posting a new note via the list view form
        response = self.client.post(reverse('note_list'), {
            'title': 'New Created Note',
            'content': 'Created via POST test.',
            'color': 'sunny yellow'
        })
        # Check that it redirects after successful post
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 2)
        self.assertTrue(Note.objects.filter(title='New Created Note').exists())