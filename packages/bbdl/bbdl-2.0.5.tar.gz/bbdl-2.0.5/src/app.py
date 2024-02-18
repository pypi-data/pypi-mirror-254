from .bbdl.bbdl import BBDL

if __name__ == "__main__":
    bb = BBDL()
    bb.get_date()
    print(bb.input_date)
    print(bb.input_date[2])
    print(bb.input_date[1])
    print(bb.input_date[0])
    bb.max_page_check(bb.input_date[2], bb.input_date[1], bb.input_date[0])
    bb.bb_dl_full(
        bb.max_pages,
        bb.input_date[2],
        bb.input_date[1],
        bb.input_date[0],
        download=False,
    )
    print(bb.list_of_urls)
