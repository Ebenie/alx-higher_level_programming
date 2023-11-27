#include "lists.h"
/**
 * check_cycle - checks if a linked list has a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
    listint_t *ptr1 = list;
    listint_t *ptr2 = list;

    if (!list)
        return 0;

    while (ptr1 != NULL && ptr2 != NULL && ptr2->next != NULL)
    {
        ptr1 = ptr1->next;
        ptr2 = ptr2->next->next;

        if (ptr1 == ptr2)
            return 1;
    }

    return 0;
}
