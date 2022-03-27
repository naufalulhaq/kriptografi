def extended_gcd(a, b):
    (old_r, r) = (a, b)
    (old_s, s) = (1, 0)
    (old_t, t) = (0, 1)

    while r != 0:
        quotient = old_r // r
        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)
        (old_t, t) = (t, old_t - quotient * t)

    return old_r, old_s, old_t

g, u, v = extended_gcd(a = 26513, b = 32321)
print(g, u, v)
print(26513 * u + 32321 * v)

#this doesnt work. idk :')
