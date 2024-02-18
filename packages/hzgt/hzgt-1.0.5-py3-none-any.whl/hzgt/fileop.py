import os
import sys

import urllib.request

from .sc import SCError

from .CONST import INSTALLCMD

try:
    from pypdf import PdfReader, PdfWriter
except Exception as err:
    print(err)
    os.system(INSTALLCMD("pypdf==3.17.2"))
    from pypdf import PdfReader, PdfWriter

try:
    from tqdm import tqdm
except Exception as err:
    print(err)
    os.system(INSTALLCMD("tqdm"))
    from tqdm import tqdm

try:
    import stepic
except Exception as err:
    print(err)
    os.system(INSTALLCMD("stepic==0.5.0"))
    import stepic

try:
    from PIL import Image
except Exception as err:
    print(err)
    os.system(INSTALLCMD("Pillow"))
    from PIL import Image


def Bit_Unit_Conversion(fsize: int):
    """
    字节单位转换

    (大小,单位,原大小)

    :param fsize: 大小
    :return: 大小,单位,原大小
    """
    if fsize < 1024:
        return fsize, 'Byte', fsize
    else:
        KBX = fsize / 1024
        if KBX < 1024:
            return round(KBX, 2), 'KB', fsize
        else:
            MBX = KBX / 1024
            if MBX < 1024:
                return round(MBX, 2), 'MB', fsize
            else:
                return round(MBX / 1024, 2), 'GB', fsize


def getdirsize(dirpath: str):
    """
    :param dirpath:目录或者文件
    :return: size: 目录或者文件的大小
    """
    size = 0
    print(os.path.isdir(dirpath), os.path.isfile(dirpath))
    if os.path.isdir(dirpath): # 如果是目录
        for root, dirs, files in os.walk(dirpath):
            size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
        return size
    elif os.path.isfile(dirpath):  # 如果是文件
        size = os.path.getsize(dirpath)
        return size
    else:
        raise SCError("目录/文件 不存在")



def getFileSize(filepath: str):
    """
    获取目录或文件的总大小

    :param filePath: 目录或者文件
    :return: 例子：(2, 'M', 2048)
    """
    fsize = getdirsize(filepath)  # 返回的是字节大小
    return Bit_Unit_Conversion(fsize)


def getUrlFileSize(url: str):
    """
    获取url上的文件的总大小

    :param url: 网络url
    :return: 例子：(2, 'M', 2048)
    """
    response = urllib.request.urlopen(url)
    file_size = int(response.headers["Content-Length"])
    return Bit_Unit_Conversion(file_size)


def AddPwd(InputPath: str, OutputPath: str, PassWord: str, BoolEnforce=False, OldPassWord: str = '', BoolBar=False):
    """
    pdf加密/修改密码
    :param InputPath: 待加密的pdf文件路径
    :param OutputPath: 输出的pdf文件路径
    :param PassWord: 添加的密码
    :param BoolEnforce: 是否强制加密【修改密码】
    :param OldPassWord: 若强制加密则需要原密码
    :param BoolBar: 是否显示进度条
    :return:
    """
    pdf_reader = PdfReader(open(InputPath, 'rb'))  # 打开pdf文件

    if pdf_reader.is_encrypted and not BoolEnforce:  # 已加密且不修改密码
        # print("该PDF文件为已加密的PDF文件")
        return None
    if pdf_reader.is_encrypted and BoolEnforce:  # 已加密且修改密码
        # print("修改密码中......")
        pdf_reader = PdfReader(open(InputPath, "rb+"), password=OldPassWord)  # 打开有密码的pdf文件
    pdf_writer = PdfWriter()  # 创建写入对象
    pdfpages = pdf_reader.pages
    if BoolBar:  # 显示进度条
        with tqdm(pdfpages, total=len(pdfpages), desc="Doing", unit="page") as bar:  # 进度条
            for page in bar:
                pdf_writer.add_page(page)
    else:  # 不显示进度条
        for page in pdfpages:
            pdf_writer.add_page(page)
    pdf_writer.encrypt(PassWord)  # 添加密码
    pdf_writer.write(open(OutputPath, 'wb'))  # 写入新文件
    return True


def TryGetPDFPwd(filename: str, pwddict: list[str], BoolBar=False):
    """
    从字典中尝试解密
    :param filename: str: pdf文件路径
    :param pwddict: list[str]: 字典
    :param BoolBar: bool: 是否显示进度条
    :return: 是否有密码-True/Flase, 是否解密成功-None/密码
    """
    pdfFile = PdfReader(open(filename, "rb"))  # 打开pdf文件

    if pdfFile.is_encrypted:  # 如果有密码
        fp = open(filename, "rb")
        if BoolBar:  # 显示进度条
            with tqdm(pwddict, total=len(pwddict), desc="Doing",  unit="word") as bar:  # 进度条
                for word in bar:
                    try:
                        bar.set_postfix(CurrentPwd=word)
                        PdfReader(fp, password=word)
                        return True, word
                    except:
                        continue
        else:  # 不显示进度条
            for word in pwddict:
                try:
                    PdfReader(fp, password=word)
                    return True, word
                except:
                    continue
        return True, None
    else:  # 如果没密码
        return False, None

def ImgEncode(inputpath: str, outputpath: str, secretmsg: str):
    """
    在图片中添加隐秘信息
    :param inputpath: str: 需要加密的图片文件路径
    :param outputpath: str: 输出图片的路径
    :param secretmsg: str: 加密内容
    :return:
    """
    gvn_image = Image.open(inputpath)
    encodedimage = stepic.encode(gvn_image, secretmsg.encode())
    encodedimage.save(outputpath)


def ImgDecode(inputpath: str):
    """
    在图片中读取加密信息
    :param inputpath: str: 图片文件路径
    :return: 解密的内容
    """
    encryptd_image = Image.open(inputpath)
    decryptedmsg = stepic.decode(encryptd_image)
    return decryptedmsg