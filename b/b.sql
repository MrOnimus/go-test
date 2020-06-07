SELECT id, name FROM goods
INNER JOIN
    ( SELECT goods_id FROM 
        ( SELECT	COUNT(tag_id) as num_of_tags, goods_id FROM tags_goods GROUP BY goods_id ) as tg,
        ( SELECT COUNT(id) as num FROM tags) as t
      WHERE tg.num_of_tags = t.num
	) as res
ON goods.id = res.goods_id

