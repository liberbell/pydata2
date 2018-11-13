import saytime

def main():
    st = saytime.saytime()
    print('\nnumbers test:')
    list = (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        12, 15, 19, 20, 30 , 50, 51, 52, 55,
        55, 59, 99, 100, 101, 112, 900, 999, 1000
    )
    for l in list:
        st.number(l)
        print(l, st.numwords())

    print('\ntime test:')
    list = (
        
    )
