package bolts;


import lombok.extern.slf4j.Slf4j;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.BasicOutputCollector;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseBasicBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;

import java.util.Map;

@Slf4j
public class WriterBolt extends BaseBasicBolt {


	@Override
	public void execute(Tuple arg0, BasicOutputCollector arg1) {
		try {
			String str = arg0.getString(0);
			String str1 = arg0.getString(1);
			log.info(str + "****" + str1 + "**** " + this);
			Thread.sleep(5000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}

	@Override
	public void prepare(Map stormConf, TopologyContext context) {
	}

	@Override
	public void declareOutputFields(OutputFieldsDeclarer arg0) {
		arg0.declare(new Fields("result"));
	}

}