# streamlit_client.py
import streamlit as st
import grpc

# 生成済みのprotoファイルをインポート
from proto_files import ai_agent_pb2, ai_agent_pb2_grpc


def run():
    st.header("gRPCでGoサーバーと通信するStreamlitクライアント")
    name = st.text_input("あなたの名前を入力してください：")

    if st.button("挨拶を送る"):
        if name:
            try:
                # Goサーバーがdocker-composeのネットワーク上で利用可能なホスト名 "go_server" を指定
                with grpc.insecure_channel("go_server:50051") as channel:
                    stub = ai_agent_pb2_grpc.AIAgentStub(channel)
                    response = stub.SayHello(ai_agent_pb2.HelloRequest(name=name))
                    st.success(f"サーバーからの応答: {response.message}")
            except grpc.RpcError as e:
                st.error(f"gRPCエラー: {e}")
        else:
            st.warning("名前を入力してください。")

    if st.button("Send balloons!"):
        st.balloons()


if __name__ == "__main__":
    st.title("StreamlitとGoのAPIサーバーをgRPCで繋いでみた👋")
    run()
