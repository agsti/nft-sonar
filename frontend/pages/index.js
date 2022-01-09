import axios from 'axios'
import Head from 'next/head'
import FileUpload from '../components/FileUploadComponent.js'
import MatchedView from '../components/MatchedView.js'
import NoMatchView from '../components/NoMatchView.js'
import NftSonarLogo from '../components/NftSonarLogo.js'
import { useState } from 'react'

export default function Home() {
    const [matches, setMatches] = useState()
    const [winner, setWinner] = useState()
    const [uploadedImage, setUploadedImage] = useState()
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
        const bestMatch = response.data[0]
        console.log(bestMatch)
        if (bestMatch.score > 0.8) {
            setWinner(bestMatch)
        }
        setMatches(response.data)
    }

    async function onDrop(drop) {
        setUploadedImage(drop[0].name)
        if (drop.length == 1) {
            upload(drop[0])
            setUploadedImage(URL.createObjectURL(drop[0]))
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
            <div className="flex px-10 flex-col min-h-screen justify-center items-center bg-hero bg-cover w-full">
                {/* <Image src="/public/vercel.svg" layout='fill'/> */}

                <NftSonarLogo />
                <FileUpload onDrop={onDrop} accept="image/*" />
                {winner ? (
                    <MatchedView winner={winner} />
                ) : (
                    matches && <NoMatchView matches={matches} />
                )}
                {/* <img src={uploadedImage} /> */}
            </div>
        </div>
    )
}
