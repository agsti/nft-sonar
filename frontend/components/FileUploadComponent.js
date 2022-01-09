import React from 'react'
// Import the useDropzone hooks from react-dropzone
import { useDropzone } from 'react-dropzone'

const Dropzone = ({ onDrop, accept }) => {
    // Initializing useDropzone hooks with options
    const { getRootProps, getInputProps, isDragActive } = useDropzone({
        onDrop,
        accept,
    })

    /* 
    useDropzone hooks exposes two functions called getRootProps and getInputProps
    and also exposes isDragActive boolean
  */

    return (
        <div
            className="p-4 my-10 border-4 border-whitish border-dashed rounded-lg"
            {...getRootProps()}
        >
            <input {...getInputProps()} />
            <div className="text-whitish text-xl">
                {isDragActive ? (
                    <p>Release to drop the files here</p>
                ) : (
                    <p>Drag &apos;n&apos; drop some files here</p>
                )}
            </div>
        </div>
    )
}

export default Dropzone
