from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note


def note_list(request):
    """Display a list of all notes and handle creation of a new note."""
    notes = Note.objects.all().order_by("-created_at")
    form = NoteForm()

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")

    context = {"notes": notes, "form": form}
    return render(request, "notes/note_list.html", context)


def note_update(request, pk):
    """Handle updating an existing Note instance.

    Retrieves the note by primary key, binds the form to the request data
    and existing instance, and saves changes upon valid submission.
    """
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)

    context = {"form": form, "note": note}
    return render(request, "notes/note_form.html", context)


def note_delete(request, pk):
    """Handle the deletion of an existing Note instance."""
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect("note_list")
    return render(request, "notes/note_confirm_delete.html", {"note": note})