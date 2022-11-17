import { Typography, Form, Input, Button, Space, message, Upload } from 'antd'
import type { UploadProps } from 'antd';
import { InboxOutlined } from '@ant-design/icons';
import './App.css'

const { Title, Paragraph } = Typography
const { Dragger } = Upload;

const props: UploadProps = {
  name: 'file',
  multiple: true,
  action: 'http://127.0.0.1:8000/uploadfile',
  onChange(info) {
    const { status } = info.file;
    if (status !== 'uploading') {
      console.log(info.file, info.fileList);
    }
    if (status === 'done') {
      message.success(`${info.file.name} file uploaded successfully.`);
    } else if (status === 'error') {
      message.error(`${info.file.name} file upload failed.`);
    }
  },
  onDrop(e) {
    console.log('Dropped files', e.dataTransfer.files);
  },
};

function App() {
  const [form] = Form.useForm();

  const onFinish = () => {
    message.success('Submit success!');
  };

  const onFinishFailed = () => {
    message.error('Submit failed!');
  };

  const onFill = () => {
    form.setFieldsValue({
      url: 'https://taobao.com/',
    });
  };

  const normFile = (e: any) => {
    console.log('Upload event:', e);
    if (Array.isArray(e)) {
      return e;
    }
    return e?.fileList;
  };

  return (
    <>
      <div className='content'>
        <Typography>
          <Title level={1}>Faceblur</Title>
          <Title level={4}>Detecção e anonimização de rostos</Title>
          <br />
          <Form
            form={form}
            layout="vertical"
            onFinish={onFinish}
            onFinishFailed={onFinishFailed}
            autoComplete="off"
          >
             <Form.Item
              name="upload"
              label="Faça o upload de uma imagem ou vídeo:"
            >
              <Form.Item name="dragger" valuePropName="fileList" getValueFromEvent={normFile} noStyle>
                <Dragger {...props}>
                  <p className="ant-upload-drag-icon">
                    <InboxOutlined />
                  </p>
                  <p className="ant-upload-text">Clique ou arraste arquivos nessa área para fazer upload</p>
                  <p className="ant-upload-hint">
                    Suporte para upload de múltiplas mídias.
                  </p>
                </Dragger>
              </Form.Item>
            </Form.Item>

            <Form.Item>
              <Space>
                <Button type="primary" htmlType="submit">
                  Submit
                </Button>
                <Button htmlType="button" onClick={onFill}>
                  Fill
                </Button>
              </Space>
            </Form.Item>
          </Form>
        </Typography>
      </div>

    </>
  );
}

export default App
