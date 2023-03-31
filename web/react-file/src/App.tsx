import React, { useState } from 'react';

import { Typography } from 'antd';
import { InboxOutlined, DownloadOutlined } from '@ant-design/icons';
import { Upload, Button } from 'antd';
import type { UploadProps } from 'antd';
import './App.css';

const { Dragger } = Upload;
const { Title, Paragraph, Text } = Typography;

const App: React.FC = () => {
  const [state, setState] = useState<'success' | 'error'>('error');
  const [resHref, setRefHref] = useState('');

  const uploadProps: UploadProps = {
    name: 'file',
    multiple: false,
    method: 'POST',
    action: 'http://127.0.0.1:9527/pdf_or_docx',
    onChange({ file, fileList, event }) {
      if (file.status !== 'uploading') {
        console.log(file, fileList);
        setState('success');
        setRefHref(`http://127.0.0.1:9527/download?file_name=${file.response.file_name}`);
      }
    },
    onDrop(e) {
      console.log('Dropped files', e.dataTransfer.files);
    },
  };
  return (
    <div className='App'>
      <Title style={{ marginBottom: 60 }}>文档格式转换</Title>
      <Paragraph style={{ marginBottom: 40 }}>
        可以把
        <Text type='success'>pdf</Text>
        格式转换成 <Text type='success'>docx</Text> , 也可以把
        <Text type='success'>docx 或者 docx</Text> 转换成 <Text type='success'>pdf</Text>
        格式
      </Paragraph>
      <Dragger {...uploadProps}>
        <p className='ant-upload-drag-icon'>
          <InboxOutlined />
        </p>
        <p className='ant-upload-text'>点击选择转换的文件 或者 把文件拖到这里</p>
      </Dragger>
      {state === 'success' ? (
        <Button
          type='primary'
          shape='round'
          icon={<DownloadOutlined />}
          size='large'
          style={{ marginTop: 30 }}
          href={resHref}
        >
          下载文件
        </Button>
      ) : (
        ''
      )}
    </div>
  );
};

export default App;
