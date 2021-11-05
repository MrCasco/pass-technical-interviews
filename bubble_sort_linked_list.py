class Nodo:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def iniciar_lista(nums):
    prev = Nodo(nums.pop(0))
    head = prev
    while nums:
        prev.next = Nodo(nums.pop(0))
        prev = prev.next
    return head

def entrar_numeros():
    n = int(input('¿Cuántos números vas a entrar?: '))
    i = 1
    nums = []
    while i <= n:
        num = int(input('Entra número '+str(i)+': '))
        nums.append(num)
        i += 1
    return nums

def bubble_sort(root):
    n_root = Nodo(float('-inf'))
    n_root.next = root
    tail = None
    last = n_root
    prev = root
    cur = root.next
    while n_root.next != tail:
        while cur != tail:
            if prev.val > cur.val:
                last.next = cur
                cur.next, prev.next = prev, cur.next
                cur = prev
            last = last.next
            prev = cur
            cur = cur.next
        tail = prev
        last = n_root
        prev = n_root.next
        cur = prev.next
    return n_root.next

def imprimir_lista(root):
    print('[', end='')
    while root:
        print(root.val, end=', ')
        root = root.next
    print(']', end='')

nums = entrar_numeros()
head = iniciar_lista(nums)
imprimir_lista(head)
