import re

##########################################################
# 字種分割
##########################################################
def divide_char_type(document, concat_conj_in_ja=True):
    re_kana = re.compile("[ぁ-ゖー～]")          # 平仮名の正規表現
    re_kata = re.compile("[ァ-ヶｦ-ｯｱ-ﾝー～]")    # カタカナの正規表現
    re_cjk = re.compile("[一-龠々]")             # 漢字の正規表現
    re_alpha = re.compile("[A-Za-zＡ-Ｚａ-ｚ]")  # アルファベットの正規表現
    re_digit = re.compile("[0-9０-９]")          # 数字の正規表現
    #re_punc = re.compile("[,，][^0-9０-９]|[^0-9０-９][,，]|、")  # 読点の正規表現
    #re_point = re.compile("[.．。!?！？]")                        # 句点の正規表現
    #re_break = re.compile("\r?\n")                                # 段落の正規表現
    #re_word = re.compile("[a-zA-ZＡ-Ｚａ-ｚ0-9０-９ぁ-ゖァ-ヶｦ-ｯｱ-ﾝー一-龠々][a-zA-ZＡ-Ｚａ-ｚ0-9０-９ぁ-ゖァ-ヶｦ-ｯｱ-ﾝ一-龠々ー～・'&.,]*$")

    text1 = document  # 全文
    #text2 = re.split(re_break, text1)   # 段落単位

    list_kana_words = []   # 平仮名の分割語リスト
    list_kata_words = []   # カタカナの分割語リスト
    list_cjk_words = []    # 漢字の分割語リスト
    list_alpha_words = []  # アルファベットの分割語リスト
    list_digit_words = []  # 数字の分割語リスト
    list_other_words = []  # その他の分割語リスト

    tmp_char_class = None  # 一つ前の文字の字種
    conj = None            # 接続記号
    conjlist = {".", "&", "．", "＆"}   # 接続記号の一覧
    end_period = {"e.g", "u.s", "u.s.a"}

    allwords = []       # 分割語リスト
    allwords_type = []  # 分割語リストの字種（0:平仮名、1:カタカナ、2:漢字、3:アルファベット、4:数字、5:その他）

    # 1文字目の処理
    # 平仮名の場合
    if re_kana.match(text1[0]) is not None:
        allwords.append(text1[0])          # 分割語の追加
        list_kana_words.append(text1[0])   # 平仮名リストへの追加
        tmp_char_class = "kana"     # 現在の文字の字種
    # カタカナの場合
    elif re_kata.match(text1[0]) is not None:
        allwords.append(text1[0])          # 分割語の追加
        list_kata_words.append(text1[0])   # カタカナリストへの追加
        tmp_char_class = "kata"     # 現在の文字の字種
    # 漢字の場合
    elif re_cjk.match(text1[0]) is not None:
        allwords.append(text1[0])          # 分割語の追加
        list_cjk_words.append(text1[0])    # 漢字リストへの追加
        tmp_char_class = "cjk"      # 現在の文字の字種
    # アルファベットの場合
    elif re_alpha.match(text1[0]) is not None:
        allwords.append(text1[0])          # 分割語の追加
        list_alpha_words.append(text1[0])  # アルファベットリストへの追加
        tmp_char_class = "alpha"    # 現在の文字の字種
    # 数字の場合
    elif re_digit.match(text1[0]) is not None:
        allwords.append(text1[0])          # 分割語の追加
        list_digit_words.append(text1[0])  # 数字リストへの追加
        tmp_char_class = "digit"    # 現在の文字の字種
    # それ以外の場合
    else:
        allwords.append(text1[0])          # 分割語の追加
        list_other_words.append(text1[0])  # その他リストへの追加
        tmp_char_class = None       # 現在の文字の字種

    # 字種分割処理
    for i in text1[1:]:
        # 一つ前が接続記号の場合
        if conj is not None:
            # 平仮名の場合
            if re_kana.match(i) is not None:
                # アルファベットや数字の後にある接続記号を前の単語に結合する場合
                if concat_conj_in_ja:
                    del allwords[-1]
                    del list_other_words[-1]
                    allwords[-1] += conj
                    if tmp_char_class == "alpha":
                        list_alpha_words[-1] += conj
                    elif tmp_char_class == "digit":
                        list_digit_words[-1] += conj
                else:
                    del list_other_words[-1]
                    list_other_words.append(conj)
                allwords.append(i)          # 分割語の追加
                list_kana_words.append(i)   # ひらがなリストへの追加
                tmp_char_class = "kana"     # 現在の文字の字種
                conj = None                 # conjの初期化
            # カタカナの場合
            elif re_kata.match(i) is not None:
                # アルファベットや数字の後にある接続記号を前の単語に結合する場合
                if concat_conj_in_ja:
                    del allwords[-1]
                    del list_other_words[-1]
                    allwords[-1] += conj
                    if tmp_char_class == "alpha":
                        list_alpha_words[-1] += conj
                    elif tmp_char_class == "digit":
                        list_digit_words[-1] += conj
                else:
                    del list_other_words[-1]
                    list_other_words.append(conj)
                allwords.append(i)          # 分割語の追加
                list_kata_words.append(i)   # カタカナリストへの追加
                tmp_char_class = "kata"     # 現在の文字の字種
                conj = None                 # conjの初期化
            # 漢字の場合
            elif re_cjk.match(i) is not None:
                # アルファベットや数字の後にある接続記号を前の単語に結合する場合
                if concat_conj_in_ja:
                    del allwords[-1]
                    del list_other_words[-1]
                    allwords[-1] += conj
                    if tmp_char_class == "alpha":
                        list_alpha_words[-1] += conj
                    elif tmp_char_class == "digit":
                        list_digit_words[-1] += conj
                else:
                    del list_other_words[-1]
                    list_other_words.append(conj)
                allwords.append(i)          # 分割語の追加
                list_cjk_words.append(i)    # 漢字リストへの追加
                tmp_char_class = "cjk"      # 現在の文字の字種
                conj = None                 # conjの初期化
            # アルファベットの場合
            elif re_alpha.match(i) is not None:
                # 二つ前がアルファベットの場合
                if tmp_char_class == "alpha":
                    del allwords[-1]
                    del list_other_words[-1]
                    allwords[-1] += conj + i          # 分割語の結合
                    list_alpha_words[-1] += conj + i  # アルファベットリストへの結合
                else:
                    allwords.append(i)          # 分割語の追加
                    list_alpha_words.append(i)  # アルファベットリストへの追加
                tmp_char_class = "alpha"    # 現在の文字の字種
                conj = None                 # conjの初期化
            # 数字の場合
            elif re_digit.match(i) is not None:
                # 二つ前が数字の場合
                if tmp_char_class == "digit":
                    del allwords[-1]
                    del list_other_words[-1]
                    allwords[-1] += conj + i          # 分割語の結合
                    list_digit_words[-1] += conj + i  # 数字リストへの結合
                else:
                    allwords.append(i)          # 分割語の追加
                    list_digit_words.append(i)  # 数字リストへの追加
                tmp_char_class = "digit"    # 現在の文字の字種
                conj = None                 # conjの初期化
            # それ以外の場合
            else:
                # 後置ピリオドの場合
                if conj == "." and allwords[-2] in end_period:
                    del allwords[-1]
                    del list_other_words[-1]
                    allwords[-1] += conj     # 分割語の結合
                    allwords.append(i)       # 分割語の追加
                    if tmp_char_class == "alpha":
                        list_alpha_words[-1] += conj
                    elif tmp_char_class == "digit":
                        list_digit_words[-1] += conj
                    list_other_words.append(i)  # その他リストへの追加
                else:
                    allwords[-1] += i              # 分割後の結合
                    list_other_words[-1] += i      # その他リストへの結合
                tmp_char_class = None       # 現在の文字の字種
                conj = None                 # conjの初期化
        # 一つ前が平仮名
        elif tmp_char_class == "kana":
            # 平仮名の場合
            if re_kana.match(i) is not None:
                allwords[-1] += i           # 分割語の結合
                list_kana_words[-1] += i    # ひらがなリストへの結合
            # カタカナの場合
            elif re_kata.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_kata_words.append(i)   # カタカナリストへの追加
                tmp_char_class = "kata"     # 現在の文字の字種
            # 漢字の場合
            elif re_cjk.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_cjk_words.append(i)    # 漢字リストへの追加
                tmp_char_class = "cjk"      # 現在の文字の字種
            # アルファベットの場合
            elif re_alpha.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_alpha_words.append(i)  # アルファベットリストへの追加
                tmp_char_class = "alpha"    # 現在の文字の字種
            # 数字の場合
            elif re_digit.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_digit_words.append(i)  # 数字リストへの追加
                tmp_char_class = "digit"    # 現在の文字の字種
            # それ以外の場合
            else:
                allwords.append(i)          # 分割語の追加
                list_other_words.append(i)  # その他リストへの追加
                tmp_char_class = None       # 現在の文字の字種
        # 一つ前がカタカナ
        elif tmp_char_class == "kata":
            # カタカナの場合
            if re_kata.match(i) is not None or i == "-" or i == "ｰ":
                allwords[-1] += i           # 分割語の結合
                list_kata_words[-1] += i    # カタカナリストへの結合
            # 平仮名の場合
            elif re_kana.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_kana_words.append(i)   # ひらがなリストへの追加
                tmp_char_class = "kana"     # 現在の文字の字種
            # 漢字の場合
            elif re_cjk.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_cjk_words.append(i)    # 漢字リストへの追加
                tmp_char_class = "cjk"      # 現在の文字の字種
            # アルファベットの場合
            elif re_alpha.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_alpha_words.append(i)  # アルファベットリストへの追加
                tmp_char_class = "alpha"    # 現在の文字の字種
            # 数字の場合
            elif re_digit.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_digit_words.append(i)  # 数字リストへの追加
                tmp_char_class = "digit"    # 現在の文字の字種
            # それ以外の場合
            else:
                allwords.append(i)          # 分割語の追加
                list_other_words.append(i)  # その他リストへの追加
                tmp_char_class = None       # 現在の文字の字種
        # 一つ前が漢字
        elif tmp_char_class == "cjk":
            # 漢字の場合
            if re_cjk.match(i) is not None:
                allwords[-1] += i           # 分割語の結合
                list_cjk_words[-1] += i     # 漢字リストへの結合
            # 平仮名の場合
            elif re_kana.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_kana_words.append(i)   # ひらがなリストへの追加
                tmp_char_class = "kana"     # 現在の文字の字種
            # カタカナの場合
            elif re_kata.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_kata_words.append(i)   # カタカナリストへの追加
                tmp_char_class = "kata"     # 現在の文字の字種
            # アルファベットの場合
            elif re_alpha.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_alpha_words.append(i)  # アルファベットリストへの追加
                tmp_char_class = "alpha"    # 現在の文字の字種
            # 数字の場合
            elif re_digit.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_digit_words.append(i)  # 数字リストへの追加
                tmp_char_class = "digit"    # 現在の文字の字種
            # それ以外の場合
            else:
                allwords.append(i)          # 分割語の追加
                list_other_words.append(i)  # その他リストへの追加
                tmp_char_class = None       # 現在の文字の字種
        # 一つ前がアルファベット
        elif tmp_char_class == "alpha":
            # アルファベットの場合
            if re_alpha.match(i) is not None:
                allwords[-1] += i           # 分割語の結合
                list_alpha_words[-1] += i   # アルファベットリストへの結合
            # 数字の場合
            elif re_digit.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_digit_words.append(i)  # 数字リストへの追加
                tmp_char_class = "digit"    # 現在の文字の字種
            # 平仮名の場合
            elif re_kana.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_kana_words.append(i)   # ひらがなリストへの追加
                tmp_char_class = "kana"     # 現在の文字の字種
            # カタカナの場合
            elif re_kata.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_kata_words.append(i)   # カタカナリストへの追加
                tmp_char_class = "kata"     # 現在の文字の字種
            # 漢字の場合
            elif re_cjk.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_cjk_words.append(i)    # 漢字リストへの追加
                tmp_char_class = "cjk"      # 現在の文字の字種
            # 接続記号の場合
            elif i in conjlist:
                conj = i                    # 接続記号の登録
                allwords.append(i)          # 分割語の追加
                list_other_words.append(i)  # その他リストへの追加
            # それ以外の場合
            else:
                allwords.append(i)          # 分割語の追加
                list_other_words.append(i)  # その他リストへの追加
                tmp_char_class = None       # 現在の文字の字種
        # 一つ前が数字
        elif tmp_char_class == "digit":
            # 数字の場合
            if re_digit.match(i) is not None:
                allwords[-1] += i           # 分割語の結合
                list_digit_words[-1] += i   # 数字リストへの結合
            # アルファベットの場合
            elif re_alpha.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_alpha_words.append(i)  # アルファベットリストへの追加
                tmp_char_class = "alpha"    # 現在の文字の字種
            # 平仮名の場合
            elif re_kana.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_kana_words.append(i)   # ひらがなリストへの追加
                tmp_char_class = "kana"     # 現在の文字の字種
            # カタカナの場合
            elif re_kata.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_kata_words.append(i)   # カタカナリストへの追加
                tmp_char_class = "kata"     # 現在の文字の字種
            # 漢字の場合
            elif re_cjk.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_cjk_words.append(i)    # 漢字リストへの追加
                tmp_char_class = "cjk"      # 現在の文字の字種
            # 接続記号の場合
            elif i in conjlist:
                conj = i                    # 接続記号の登録
                allwords.append(i)          # 分割語の追加
                list_other_words.append(i)  # その他リストへの追加
            # それ以外の場合
            else:
                allwords.append(i)          # 分割語の追加
                list_other_words.append(i)  # その他リストへの追加
                tmp_char_class = None       # 現在の文字の字種
        # 一つ前がそれ以外
        else:
            # 平仮名の場合
            if re_kana.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_kana_words.append(i)   # ひらがなリストへの追加
                tmp_char_class = "kana"     # 現在の文字の字種
            # カタカナの場合
            elif re_kata.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_kata_words.append(i)   # カタカナリストへの追加
                tmp_char_class = "kata"     # 現在の文字の字種
            # 漢字の場合
            elif re_cjk.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_cjk_words.append(i)    # 漢字リストへの追加
                tmp_char_class = "cjk"      # 現在の文字の字種
            # アルファベットの場合
            elif re_alpha.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_alpha_words.append(i)  # アルファベットリストへの追加
                tmp_char_class = "alpha"    # 現在の文字の字種
            # 数字の場合
            elif re_digit.match(i) is not None:
                allwords.append(i)          # 分割語の追加
                list_digit_words.append(i)  # 数字リストへの追加
                tmp_char_class = "digit"    # 現在の文字の字種
            # それ以外の場合
            else:
                allwords[-1] += i           # 分割語の追加
                list_other_words[-1] += i   # その他リストへの追加
                tmp_char_class = None       # 現在の文字の字種

    for i in allwords:
        # 平仮名の場合
        if re_kana.match(i[0]) is not None:
            allwords_type.append(0)
        # カタカナの場合
        elif re_kata.match(i[0]) is not None:
            allwords_type.append(1)
        # 漢字の場合
        elif re_cjk.match(i[0]) is not None:
            allwords_type.append(2)
        # アルファベットの場合
        elif re_alpha.match(i[0]) is not None:
            allwords_type.append(3)
        # 数字の場合
        elif re_digit.match(i[0]) is not None:
            allwords_type.append(4)
        # それ以外の場合
        else:
            allwords_type.append(5)

    # 戻り値（字種分割語リスト、字種分割語字種タイプリスト、
    #         平仮名連リスト、カタカナ連リスト、漢字連リスト、
    #         アルファベット連リスト、数字連リスト、その他連リスト）
    return (allwords, allwords_type, list_kana_words, list_kata_words,
            list_cjk_words, list_alpha_words, list_digit_words, list_other_words)


############################
# main 処理
############################
if __name__ == "__main__":
    print(divide_char_type("1.0 is number.")[0])
    print(divide_char_type("1,000 is number.")[0])
    print(divide_char_type("u.s.a. is state.")[0])
    print(divide_char_type("u.k. is state.")[0])
    print(divide_char_type("e.g., th, ch, sh, ph, gh, ng, qu")[0])
    print(divide_char_type("state include u.s. u.s. is state.")[0])
    print(divide_char_type("state include u.k. u.k. is state.")[0])
    print(divide_char_type("u.s.は国です。")[0])
    print(divide_char_type("u.s.は国です。", concat_conj_in_ja=False)[0])
    print(divide_char_type("あいうえおーかきくけこ")[0])
    print(divide_char_type("アイウエオーカキクケコ")[0])
    print(divide_char_type("今日の天気は晴れです。\n明日の天気は曇りです。\n")[0])
    print(divide_char_type("&&&1.0&&&")[0])
