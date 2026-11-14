from pathlib import Path
import shutil
#1.判断文件类型，并返回对应的分类文件夹名称
def classify_file(file):
    suffix=file.suffix.lower()
    if suffix==".txt":
        return "文本文件"
    elif suffix==".csv":
        return "表格文件"
    elif suffix==".pdf":
        return "PDF文件"
    elif suffix in [".jpg",".jpeg",".png",".gif"]:
        return "图片文件"
    elif suffix==".docx":
        return "Word文件"
    elif suffix==".xlsx":
        return "Excel文件"
    elif suffix==".zip":
        return "压缩文件"
    elif suffix==".mp4":
        return "视频文件"
    elif suffix==".py":
        return "代码文件"
    else:
        return "其他文件"


#2.扫描文件夹，获取所有文件
def scan_files(folder):
    if not folder.exists():
        print("原始文件夹不存在")
        return []
    files=[]
    for file in folder.iterdir():
        if file.is_file():
            files.append(file)
    return files

#3.复制文件到对应的分类文件夹
def organize_files(files,output_folder):
    counts={}
    for file in files:
        category=classify_file(file)
        category_folder=output_folder / category
        category_folder.mkdir(parents=True, exist_ok=True)
        target_file=category_folder / file.name
        try:
            shutil.copy2(file,target_file)
            print("整理成功：",file.name,"->",category)
            counts[category]=counts.get(category,0)+1
        except Exception as e:  
            print("整理失败：",file.name)
            print("错误原因：",e)  
    return counts


#4.生成整理报告
def create_report(counts,output_folder):
    report_file=output_folder / "整理报告.txt"
    content="Python自动文件整理报告\n"
    content+="-------------------------------\n"
    total=0
    for category, number in counts.items():
        content+=category+":"+str(number)+"个\n"
        total+=number
    content+="-------------------------------\n"
    content+="成功整理文件总数:"+str(total)+"个\n"
    report_file.write_text(content,encoding="utf-8")
    print("\n整理报告已成功生成")


#5.主程序
if __name__=="__main__":
    source_folder=Path("test_files")
    output_folder=Path("output")
    output_folder.mkdir(exist_ok=True)
    print("开始扫描文件....\n")
    files=scan_files(source_folder)
    if files:
        print("一共发现",len(files),"个文件。\n")
        counts=organize_files(files,output_folder)
        create_report(counts,output_folder) 
        print("\n全部任务完成！")
    else:
        print("没有发现任何文件，请检查test_files文件夹。")

              