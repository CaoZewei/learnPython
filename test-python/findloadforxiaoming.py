total_time = 0
r, y, g = map(int, input().split())
n = int(input())
for i in range(n):
    m_type, m_time = map(int, input().split())
    print('m_time', m_time)
    if m_type == 0:
        total_time += m_time
        print('total time', total_time)
        continue
    if m_type == 1:
        m_time += g
        m_type = 3
    if m_type == 2:
        m_time += (r + g)
        m_type = 3
    if m_type == 3:
        pass
    print('m_time end', m_time)
    now_time = (m_time - total_time) % (g+r+y)
    print('now time', now_time)
    if now_time > g:
        total_time += (now_time - g)
    print('total time', total_time)
print(total_time)
