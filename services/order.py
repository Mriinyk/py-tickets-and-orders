from typing import Optional, Any
from django.db import transaction
from django.db.models import QuerySet

from db.models import Order, User, Ticket


@transaction.atomic
def create_order(
        tickets: list[dict[str, Any]],
        username: str,
        date: Optional[str] = None,
) -> Order:
    user = User.objects.get(username=username)

    # Спочатку створюємо замовлення у базі
    order = Order.objects.create(user=user)

    # Якщо дату передано, перезаписуємо її поверх автоматичної (це вже операція оновлення)
    if date:
        order.created_at = date
        order.save()

    for ticket_data in tickets:
        Ticket.objects.create(
            row=ticket_data["row"],
            seat=ticket_data["seat"],
            movie_session_id=ticket_data["movie_session"],
            order=order,
        )

    return order


def get_orders(username: Optional[str] = None) -> QuerySet[Order]:
    queryset = Order.objects.all()
    if username:
        queryset = queryset.filter(user__username=username)
    return queryset
