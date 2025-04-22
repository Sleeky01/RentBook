from django.shortcuts import render, get_object_or_404, redirect
from .models import Rentbook
from .forms import Rentbook as rentbookForm
from django.db.models import Q

# แสดงรายการเช่าหนังสือ + ค้นหา
def rentbook_list(request):
    query = request.GET.get('q', '')
    rentbooks = Rentbook.objects.all()

    if query:
        rentbooks = rentbooks.filter(
            Q(book_title__icontains=query) |
            Q(renter_name__icontains=query) |
            Q(rent_date__icontains=query)
        )

    context = {
        'rentbooks': rentbooks,
        'query': query,
    }
    return render(request, 'rentbook_list.html', context)

# เพิ่มข้อมูลการเช่า
def rentbook_create(request):
    if request.method == 'POST':
        form = rentbookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rentbook_list')
    else:
        form = rentbookForm()

    return render(request, 'rentbook_form.html', {'form': form})

# แก้ไขข้อมูลการเช่า
def rentbook_edit(request, pk):
    book = get_object_or_404(Rentbook, pk=pk)
    if request.method == 'POST':
        form = rentbookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('rentbook_list')
    else:
        form = rentbookForm(instance=book)

    return render(request, 'rentbook_form.html', {'form': form})

# ลบข้อมูลการเช่า
def rentbook_delete(request, pk):
    book = get_object_or_404(Rentbook, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('rentbook_list')
    return render(request, 'rentbook_confirm_delete.html', {'rentbook': book})
