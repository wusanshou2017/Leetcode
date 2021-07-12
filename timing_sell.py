# 输入: [7,1,5,3,6,4]
# 输出: 5
# 输入: [7,6,4,3,1]
# 输出: 0
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit


so = Solution()

print(so.maxProfit([7, 1, 5, 3, 6, 4]))


def pipe_line_predict(file_path: str):
    f_src = open("xxxx", "r", encoding="utf-8")
    src_lst = f_src.readlines()
    src_lst = [line[:-1] for line in src_lst]
    return src_lst


def evaluate(sentence):
    attention_plot = np.zeros((max_length_targ, max_length_inp))

    sentence = "<start> " + sentence + " <end>"

    inputs = [src_tokenizer.word_index[i] for i in sentence.split(' ')]
    inputs = tf.keras.preprocessing.sequence.pad_sequences([inputs],
                                                           maxlen=max_length_inp,
                                                           padding='post')
    inputs = tf.convert_to_tensor(inputs)

    result = ''

    hidden = [tf.zeros((1, units))]
    enc_out, enc_hidden = encoder(inputs, hidden)

    dec_hidden = enc_hidden
    dec_input = tf.expand_dims([tgt_tokenizer.word_index['<start>']], 0)

    for t in range(max_length_targ):
        predictions, dec_hidden, attention_weights = decoder(dec_input,
                                                             dec_hidden,
                                                             enc_out)

        # storing the attention weights to plot later on
        attention_weights = tf.reshape(attention_weights, (-1,))
        attention_plot[t] = attention_weights.numpy()

        predicted_id = tf.argmax(predictions[0]).numpy()

        result += tgt_tokenizer.index_word[predicted_id] + ' '

        if tgt_tokenizer.index_word[predicted_id] == '<end>':
            return result, sentence, attention_plot

        # the predicted ID is fed back into the model
        dec_input = tf.expand_dims([predicted_id], 0)

    return result, sentence, attention_plot


def translate(sentence):
    result, sentence, attention_plot = evaluate(sentence)

    print('Input: %s' % (sentence))
    print('Predicted translation: {}'.format(result))

    return result
    # attention_plot = attention_plot[:len(result.split(' ')), :len(sentence.split(' '))]
    # plot_attention(attention_plot, sentence.split(' '), result.split(' '))


src_lst = pipe_line_predict("xxxxx")
predict = map(translate, src_lst)


f_predict = open("predict_res", "w+", encoding="utf-8")

predict = [line + "\n" for line in predict]

f_predict.writelines(predict)
