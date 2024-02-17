import kytest


if __name__ == '__main__':
    # 执行多个用例文件，主程序入口

    kytest.main(
        path="tests/test_adr.py",
        serial=["UJK0220521066836", "30301cb9"],
        package="com.qizhidao.clientapp",
        strategy="split_parallel"
    )


