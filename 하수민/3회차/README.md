# Node.js와 Docker를 이용한 MongoDB 사용 가이드

## 도커 설치

Docker Desktop은 Mac용 Docker를 설치하는 가장 쉬운 방법입니다.

1. [공식 Docker 사이트](https://www.docker.com/products/docker-desktop)에서 Mac 용 Docker Desktop 설치 프로그램을 다운로드 받습니다.

2. `.dmg` 파일을 클릭하여 실행시키면 설치 마법사가 시작됩니다.

3. 설치 마법사의 지시에 따라 설치를 진행합니다.

4. 설치가 완료되면 Docker Desktop을 실행합니다.

5. 터미널에서 `docker version` 명령어를 실행하여 Docker가 정상적으로 설치되었는지 확인합니다.

## Docker Compose 설치

Docker Desktop에는 Docker Compose가 이미 포함되어 있습니다. 따라서 별도의 설치 과정 없이 바로 Docker Compose를 사용할 수 있습니다.

터미널에서 `docker-compose version` 명령어를 실행하여 Docker Compose가 정상적으로 설치되었는지 확인할 수 있습니다.

## Docker Compose로 MongoDB 설치

`docker-compose.yml` 파일을 작성하여 MongoDB를 실행할 수 있습니다.

```yaml
version: '3.1'
services:
  db:
    image: mongo
    restart: always
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example
    ports:
      - 27017:27017
```

## 몽고디비 클라이언트 툴
- https://www.mongodb.com/try/download/shell

## Node.js에서 MongoDB 연결

Node.js에서 MongoDB에 연결하려면 `mongodb` 패키지를 설치해야 합니다. 아래의 명령어를 터미널에서 실행하여 `mongodb` 패키지를 설치합니다:

```bash
npm install mongodb
```

설치 후, 아래의 JavaScript 코드를 작성하여 MongoDB에 연결할 수 있습니다:

```javascript
import { MongoClient } from 'mongodb';

const uri = "mongodb://root:example@localhost:27017";

const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

client.connect()
      .then(cli => {
        console.log('connected', cli);
            
        })
```


## Node.js에서 MongoDB CRUD 코드 작성

아래는 MongoDB에서 간단한 CRUD 연산을 수행하는 코드의 예시입니다:

```javascript
import { MongoClient } from 'mongodb';

const uri = "mongodb://root:example@localhost:27017";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

async function run() {
    try {
        // Connect to MongoDB
        await client.connect();

        const collection = client.db("test").collection("documents");

        // Create
        const doc = {name: 'Test', description: 'Just testing'};
        await collection.insertOne(doc);
        console.log('Document inserted');

        // Read
        const docs = await collection.find({}).toArray();
        console.log('Found the following records');
        console.log(docs);

        // Update
        const filter = { name: 'Test' };
        const updateDoc = { $set: { description: 'Updated testing' }};
        await collection.updateOne(filter, updateDoc);
        console.log('Document updated');

        // Delete
        await collection.deleteOne(filter);
        console.log('Document deleted');

    } catch (err) {
        console.error('Error with MongoDB operations', err);
    } finally {
        await client.close();
    }
}

run().catch(console.dir);
```
