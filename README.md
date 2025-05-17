## 起動方法

### 1. ビルド

```bash
docker compose build
```

### 2. 起動

```bash
docker compose up
```

また、ビルドと起動を一度に行う場合は以下のコマンドを実行する

```bash
docker compose up --build
```

## protoファイルの作成、コード生成方法について

```
$ protoc --go_out=paths=source_relative:./go_backend/proto_files --go-grpc_out=paths=source_relative:./go_backend/proto_files -I common common/ai_agent.proto
```

```
$ python -m grpc_tools.protoc -I common --python_out=./streamlit_frontend/proto_files --grpc_python_out=./streamlit_frontend/proto_files common/ai_agent.proto
```
# streamlit_and_agent_sdk_go
