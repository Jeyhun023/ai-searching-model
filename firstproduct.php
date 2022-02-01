
        // for($x = 0; $x <= 236113; $x += 1000){
        //     $threads = Thread::with(['user', 'product'])->where('id', '<=', $x + 1000)->where('id', '>', $x)->get();
        //     // $client = ClientBuilder::create()->setRetries(2)->setHosts($this->hosts)->build();

        //     foreach($threads as $thread) {
        //         $thread = new ThreadResource($thread);
        //         event(new ThreadElasticEvent($thread));
                // if($thread->answers->isNotEmpty()){
                //     if($thread->answers->first()->linked->isNotEmpty()){
                //         foreach($thread->answers->first()->linked as $linked){
                //             $linked->delete();
                //         }
                //     }
                //     if($thread->answers->first()->comments->isNotEmpty()){
                //         foreach($thread->answers->first()->comments as $comment){
                //             $comment->delete();
                //         }
                //     }
                //     $thread->answers->first()->delete();   
                //     $thread->decrement('answer_count');
                // }

                // $tags = collect(json_decode($thread->getRawOriginal('tags')));
                // $thread->tags = $tags;
                // $thread->save();

                // $params['index'] = 'threads';
                // $params['id'] = $thread->id;
                // $params['body']['title'] = $thread->title;
                // $params['body']['slug'] = $thread->slug;
                // $params['body']['content'] = $thread->content;
                // $params['body']['tags'] = $thread->tags;
                // $params['body']['type'] = $thread->type;
                // $params['body']['user'] = $thread->user;
                // $params['body']['category'] = $thread->category;
                // $params['body']['product'] = $thread->product;
                // $params['body']['accepted_answer_id'] = $thread->accepted_answer_id;
                // $params['body']['upvote'] = $thread->upvote;
                // $params['body']['comment_count'] = $thread->comment_count;
                // $params['body']['view_count'] = $thread->view_count;
                // $params['body']['answer_count'] = $thread->answer_count;
                // $params['body']['last_active_at'] = $thread->last_active_at;
                // $params['body']['created_at'] = $thread->created_at;
                // $params['body']['updated_at'] = $thread->updated_at;
                // $params['body']['closed_at'] = $thread->closed_at;
                // $params['body']['deleted_at'] = $thread->deleted_at;
        
                // $client->index($params);

                // echo $thread->id. PHP_EOL;
            // }
        // }