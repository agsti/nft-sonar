import axios from 'axios'
import Head from 'next/head'
import FileUpload from '../components/FileUploadComponent.js'
import ClosestMatchesViewer from '../components/ClosestMatchesViewer.js'
import { useState } from 'react'

export default function Home() {
    const [matches, setMatches] = useState()
    async function upload(file, onUploadProgress) {
        var formData = new FormData()
        formData.append('file', file)
        var response = await axios.post(
            'http://localhost:8000/upload-file',
            formData,
            {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            }
        )
        console.log(response.data)
        setMatches(response.data)
    }

    async function onDrop(drop) {
        if (drop.length == 1) {
            upload(drop[0])
        }
    }

    return (
        <div className="font-default">
            <Head>
                <title>NFT-SONAR</title>
                <meta
                    name="description"
                    content="Nft sonar is a platform that allows to find NFT's in the wild"
                />
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <div className="absolute top-0 left-0 h-screen flex flex-col justify-center items-center bg-hero bg-cover w-full">
                {/* <Image src="/public/vercel.svg" layout='fill'/> */}

                <h1 className="text-7xl font-bold my-10 text-whitish">
                    NFT Sonar
                </h1>
                <FileUpload onDrop={onDrop} accept="image/*" />
                {matches && <ClosestMatchesViewer matches={matches} />}
            </div>
        </div>
    )
}
