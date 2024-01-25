package bolts;


import com.alibaba.fastjson.JSON;
import dto.BookDTO;
import org.apache.storm.shade.org.apache.commons.lang.StringUtils;
import org.apache.storm.topology.BasicOutputCollector;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseBasicBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class OutputBolt extends BaseBasicBolt {
	private static final Logger log = LoggerFactory.getLogger(OutputBolt.class);
	@Override
	public void execute(Tuple tuple, BasicOutputCollector collector) {
		try {
			String msg=tuple.getString(0);
			log.info("OutputBolt execute tuple {} ",msg);
			BookDTO bookDTO = JSON.parseObject(msg, BookDTO.class);
			if(StringUtils.isEmpty(bookDTO.getBookName())){
				log.info("bookName");
			}
			collector.emit(new Values(msg,bookDTO.getBookName()));
		} catch (Exception e) {
			e.printStackTrace();
		}

	}
 
	@Override
	public void declareOutputFields(OutputFieldsDeclarer declare) {
		declare.declare(new Fields("bookDTO","bookName"));
	}
}
