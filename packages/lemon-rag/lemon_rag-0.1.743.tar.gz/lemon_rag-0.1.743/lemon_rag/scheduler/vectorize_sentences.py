from lemon_rag.dependencies.data_access import data_access
from lemon_rag.dependencies.vector_access import embed_sentence, vector_access
from lemon_rag.lemon_runtime import models
from lemon_rag.utils import log


def vectorize_sentences():
    # 搜索所有未向量化的文件，执行向量化操作。
    files = data_access.find_file_not_vectorized()
    if not any(files):
        log.info("All existed files are vectorized")
    for file in files:
        log.info("start vectorize the sentences of the file, id=%s, filename=%s", file.id, file.origin_filename)
        for index, sentence in enumerate(file.sentences.where(models.KnowledgeSentence.vectorized == False)):
            vectors = embed_sentence([sentence.raw_content])
            vector_access.save_sentence(sentence, vectors[0])
            sentence.vectorized = True
            sentence.save(only=["vectorized"])
            if index % 10 == 0:
                data_access.update_file_vectorized_count(file)
        data_access.update_file_vectorized_count(file)
