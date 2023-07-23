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
