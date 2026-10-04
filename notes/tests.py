from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteModelTests(TestCase):
    """Test suite for the Note model and its views."""

    def setUp(self):
        """Set up initial test data."""
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note content.",
            color="light cloud"
        )

    def test_note_string_representation(self):
        """Test that the note string representation matches the title."""
        self.assertEqual(str(self.note), "Test Note")

    def test_note_list_view(self):
        """Test that the note list view loads successfully and shows notes."""
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        self.assertTemplateUsed(response, 'notes/note_list.html')

    def test_note_create_view(self):
        """Test creating a new note via POST request to note_list."""
        response = self.client.post(reverse('note_list'), {
            'title': 'New Note',
            'content': 'Brand new content',
            'color': 'sunny yellow'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect on success
        self.assertEqual(Note.objects.count(), 2)
        self.assertTrue(Note.objects.filter(title='New Note').exists())

    def test_note_update_view(self):
        """Test updating an existing note."""
        response = self.client.post(reverse('note_update', args=[self.note.pk]), {
            'title': 'Updated Title',
            'content': 'Updated content.',
            'color': 'mint green'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Title')
        self.assertEqual(self.note.color, 'mint green')

    def test_note_delete_view(self):
        """Test deleting an existing note."""
        response = self.client.post(reverse('note_delete', args=[self.note.pk]))
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertEqual(Note.objects.count(), 0)