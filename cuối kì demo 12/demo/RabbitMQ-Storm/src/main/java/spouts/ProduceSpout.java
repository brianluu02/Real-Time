package spouts;


import org.apache.storm.spout.SpoutOutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseRichSpout;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Values;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Map;
import java.util.Random;

public class ProduceSpout extends BaseRichSpout {
	private static final Logger log = LoggerFactory.getLogger(ProduceSpout.class);
	private SpoutOutputCollector collector;
	@Override
	public void nextTuple() {
		String[] str1=new String[]{"aaa","bbb","ccc","ddd"};
		String[] str2=new String[]{"ee","ff","gg","kk"};
		Random random=new Random();
		String word1=str1[random.nextInt(str1.length)];
		String word2=str2[random.nextInt(str2.length)];
		log.info("******************************开始发送数据*****************************************");
		collector.emit(new Values(word1,word2));
		try {
			Thread.sleep(3000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
 
	@Override
	public void open(Map arg0, TopologyContext arg1, SpoutOutputCollector collector) {
		this.collector=collector;
	}
	@Override
	public void declareOutputFields(OutputFieldsDeclarer arg0) {
		arg0.declare(new Fields("ppee","ttt"));
	}
}
