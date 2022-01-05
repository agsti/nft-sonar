import axios from "axios"
import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import FileUpload from '../components/FileUploadComponent.js'
import BestMatchesViewer from '../components/BestMatchesViewer.js'
import {useState} from "react"

export default function Home() {

    const [bestMatches, setBestMatches] = useState();
    async function upload(file, onUploadProgress) {
        var formData = new FormData()
        formData.append('file', file)
        var response = await axios.post("http://localhost:8000/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          }
        });
        console.log(response.data)
        setBestMatches(response.data)
      }

    async function onDrop(drop){
        console.log("DROP")
        console.log(drop)
        if (drop.length == 1){
            upload(drop[0])
        }
    }

  return (
    <div className={styles.container}>
      <Head>
        <title>NFT-SONAR</title>
        <meta name="description" content="Nft sonar is a platform that allows to find NFT's in the wild" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
            NFT Sonar
        </h1>

          <FileUpload 
                onDrop={onDrop}
              accept="image/*"
          />
          {bestMatches && <BestMatchesViewer bestMatches={bestMatches} />}


      </main>

    </div>
  )
}
