import React from "react";
// Import the useDropzone hooks from react-dropzone
import { useDropzone } from "react-dropzone";

import styles from "./FileUploadComponent.module.css"

const Dropzone = ({ onDrop, accept }) => {
  // Initializing useDropzone hooks with options
  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept
  });

  /* 
    useDropzone hooks exposes two functions called getRootProps and getInputProps
    and also exposes isDragActive boolean
  */

    const getClassName = ( isActive) => {
      if (!isActive) return styles.dropzone
      return [styles.dropzoneActive, styles.dropzone]
    };

  return (
    <div className={getClassName(isDragActive)} {...getRootProps()}>
      <input className={styles.DropzoneInput} {...getInputProps()} />
      <div className={styles.textCenter}>
        {isDragActive ? (
          <p className={styles.dropzoneContent}>Release to drop the files here</p>
        ) : (
          <p className={styles.dropzoneContent}>
            Drag &apos;n&apos; drop some files here, or click to select files
          </p>
        )}
      </div>
    </div>
  );
};

export default Dropzone;
