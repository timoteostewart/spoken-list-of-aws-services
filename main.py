import tts


def main():
    lines = None
    with open("list.txt", encoding="utf-8", mode="r") as fin:
        lines = fin.read().splitlines()

    subs = {}
    reading_subs = True

    processed_text = ""

    for line in lines:
        line = line.lower()
        if reading_subs:
            if line:
                if line == "---":
                    reading_subs = False
                else:
                    before, after = line.split(": ")
                    subs[before] = after
        else:  # not reading_subs anymore
            tokens = line.split(" ")
            cur_line = []
            for cur_token in tokens:
                if cur_token == "-":
                    cur_line.append("The next category of A.W.S. services is")
                elif cur_token in subs:
                    cur_line.append(subs[cur_token])
                else:
                    cur_line.append(cur_token)
            processed_text += " ".join(cur_line) + "\n"
    # print(processed_text)
    tts.save_text_to_mp3(processed_text, "list-of-aws-services-2022-11-29.mp3")
    return 0


if __name__ == "__main__":
    exit(main())
